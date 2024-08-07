import json
from datetime import datetime, timedelta
import zoneinfo
import os, time

os.environ['TZ'] = 'Europe/Oslo'
if hasattr(time, 'tzset'):
    time.tzset()

def escape(strng):
    #\& \% \$ \# \_ \{ \}
    #~ \textasciitilde
    #^ \textasciicircum
    #\ \textbackslash
    if not isinstance(strng, str):
        return strng
    #strng = strng.replace("µ", "\mu")
    strng = strng.replace("&","\&")
    strng = strng.replace("%","\%")
    strng = strng.replace("$","\$")
    strng = strng.replace("#","\#")
    strng = strng.replace(" _ "," \_ ")
    strng = strng.replace("{","\{")
    strng = strng.replace("}","\}")
    strng = strng.replace("~", "\textasciitilde")
    strng = strng.replace("^", "\textasciicircum")
    strng = strng.replace("\\n", "\\\\")
    strng = strng.replace(" \\ ", " \textbackslash ")
    return strng


def create_testgroup(fp, type_id, test_group):
    # Gets a single testgroup from the dictionary created from the JSON testfile
    # then creates latex and inserts into the main file that contains the extra information
    # F-String has to be escaped hence code looks a bit ugly

    tgroup_id = escape(test_group['group_id'])
    tgroup_title = f"{type_id}.{tgroup_id}: {escape(test_group['group_name'])}"
    
    rationale = escape(test_group['rationale'])
    description = escape(test_group['description'])
    comment = escape(test_group["comment"])
    
    fp.write(f'\\section{{{tgroup_title}}}\n\n')
    fp.write(f'\\subsection*{{Rationale}}\n\n')
    fp.write(f'{rationale}\n\n')
    if description.strip() != '':
        fp.write(f'\\subsection*{{Test description}}\n\n')
        fp.write(f'{description}\n\n')
    if comment.strip() != '':
        fp.write(f'\\subsection*{{Additional information}}\n\n')
        fp.write(f'{comment}\n\n')
    fp.write('\\section*{Test within this testgroup}\n\n')

    # This section generates information on each test
    for test in test_group['tests']:
        tid = escape(f"{type_id}.{tgroup_id}.{test['test_id']}  {test['name']}")
        t_text = escape(test["description"])
        t_max_power = escape(test["max_power_w"])
        t_min_power = escape(test["min_power_w"])
        t_bands = escape(test["constellation_bands"])
        t_equipment =  escape(test["equipment"])

        fp.write(f'\\subsection{{{tid}}}\n\n')
        fp.write('\\textcolor{lightgray}{\\noindent\\rule[0.5ex]{\linewidth}{1pt} }\n')
        
        
        fp.write(f'{t_text}\n')
        fp.write(f'\\subsubsection*{{Power or power range}}\n')
        fp.write(f'Min: {t_min_power}W'+"\\\\")
        fp.write(f'Max: {t_max_power}W')
        fp.write(f'\\subsubsection*{{Test bands/constellation}}\n')
        fp.write(f'{t_bands}\n'.replace('[','').replace(']',''))
        fp.write(f'\\subsubsection*{{Transmitter equpment}}\n')
        fp.write(f'{t_equipment}\n'.replace('[','').replace(']',''))
        fp.write('\\\\')

def findTestInCatalog(catalog, testId):
    resTest = {}
    my_id = testId.split(".")
    my_type = int(my_id[0])
    my_group = int(my_id[1])
    my_test = int(my_id[2])
    for type in catalog['test_types']:
        if type['type_id'] == my_type:
            resTest['type_name'] = type['type']
            for group in type['test_groups']:
                if group['group_id'] == my_group:
                    resTest['group_name'] = group['group_name']
                    for test in group['tests']:
                        if test['test_id'] == my_test:
                            resTest["full_id"] = testId
                            resTest["testObj"] = test
    if 'type_name' not in resTest:
        print("could not find test type in catalog:"+str(my_type))
    if 'group_name' not in resTest:
        print("could not find test group in catalog:"+str(my_group))
    if "full_id" not in resTest:
        print("could not find test id in catalog:"+str(testId))
    else:
        print("found test in catalog: ("+str(testId)+")")
    return resTest

#json_cat = open('testcatalog.json')
#cat = json.load(json_cat)
#print(findTestInCatalog(cat, "1.1.1"))
#exit()
def getTime(isoStr):
    return datetime.fromisoformat(isoStr).astimezone(tz=zoneinfo.ZoneInfo('CET'))

def findTestInHour(locationObj, hour):
    foundTests = []
    for test in locationObj['tests']:
        startTime = getTime(test['start_time'])
        test['start_time_t'] = startTime.strftime('%H:%M')
        endTime = getTime(test['end_time'])
        test['end_time_t'] = endTime.strftime('%H:%M')
        if int(startTime.strftime("%H")) == hour:
            foundTests.append(test)
    return foundTests

def printTest(testArr):  
    res = "{"
    for test in testArr:
        testInfo = findTestInCatalog(cat, test["test_id"])
        if "full_id" not in testInfo:
            print("Cant add test "+str(test["test_id"])+" not available in catalog")
            return "{test "+str(test["test_id"])+" not found in catalog}"
        res += f'\\normalsize{{\\textbf{{{test["start_time_t"]}-{test["end_time_t"]} - {testInfo["full_id"]} \\\\ {testInfo["testObj"]["name"]} }} }} \\\\ \n \\vspace{{1mm}} '
        if test['power_w'] > 0:
            res += f'\\footnotesize{{\hspace{{3mm}}Power: {test["power_w"]}W }} \\\\ \n'
        if test['comment'] != '':
            res += f'\\footnotesize{{\hspace{{3mm}}Comment: {test["comment"]} }} \\\\ \n'
        if test['test_contact'] != '':
            res += f'\\footnotesize{{\hspace{{3mm}}Contact: {test["test_contact"]} }} \\\\ \n'
        if testArr[len(testArr)-1] != test:
            res += f' \\hrulefill \\\\' 
    res += "}"
    return res


'''
json_mon = open('plan-monday-2024-09-09.json')
jsn = json.load(json_mon)
loc = jsn['locations'][0]
findTestInHour(loc, 11)
exit()'''
       
def create_daytable(tp, dayname, locArr):
    numOfLocs = len(locArr)
    tp.write('Start time: & ')
    for l in range(0,numOfLocs):
        localtime = datetime.fromisoformat(locArr[l]["tests"][0]['start_time']).astimezone(tz=zoneinfo.ZoneInfo('CET'))
        tp.write(str(localtime.strftime('%H:%M')))
        if l < numOfLocs-1:
            tp.write(' & ')
        else:
            tp.write(' \\\\ \hline \n')
    # each hour:
    for i in range(0,10):
        hr = i+8
        tp.write(f"{{{hr:02d}:00}} & ")
        # each location:
        for l in range(0,numOfLocs):
            testsInHour = findTestInHour(locArr[l], hr)
            #print(testsInHour)
            if len(testsInHour) > 0:
                tp.write(printTest(testsInHour))
            else:
                tp.write(' ')
            if l < numOfLocs-1:
                tp.write(' & ')
            else:
                tp.write(' \\\\  \n')


def writeTestPlan(dayname, date, dayjson):
    # create a text file for writing
    with open(f'./Latex/transmissionplan/plan-{dayname}.tex', 'w') as tp:
        tp.write('% Content below is autogenerated \n')
        # Create table for the day:
        tp.write('\\begin{longtblr}[caption={'+dayname.capitalize()+'}]{colspec={|Q[2.5cm]')
        for loc in dayjson["locations"]:
            tp.write('|Q[7cm]')
        tp.write('|},rowhead=2,cell{even[4-Z]}{1-Z}={lightlightgray},rows={halign=l}}\n')
        # add day and date:
        tp.write('\\large{'+dayname.capitalize()+'} &\\\\ \n')
        tp.write('\\footnotesize{'+date+'} ')
        # add sitenames/ids:
        for loc in dayjson["locations"]:
            tp.write('& '+loc['location_name']+'('+str(loc['location_id'])+') ')
        tp.write('\\\\ \\hline \n')
        # add all entries:
        create_daytable(tp, dayname, dayjson["locations"])
        tp.write('\n\\end{longtblr}')

# Opening JSON file with description of all tests and return dictionary for input to latex document
# get test catalog:
json_cat = open('testcatalog.json')
cat = json.load(json_cat)

json_mon = open('plan-monday-2024-09-09.json')
writeTestPlan('monday', '2024-09-09', json.load(json_mon))
