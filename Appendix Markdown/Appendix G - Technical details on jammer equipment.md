# Contents

[Appendix G - Technical details on jammer equipment](#appendix-g---technical-details-on-jammer-equipment)




[Technical details on low-power jammer “S1.1”](#technical-details-on-low-power-jammer-s11)

[Technical details on low-power jammer “S1.2”](#technical-details-on-low-power-jammer-s12)

[Technical details on low-power jammer “S1.3”](#technical-details-on-low-power-jammer-s13)

[Technical details on low-power jammer “S2.1”](#technical-details-on-low-power-jammer-s21)

[Technical details on low-power jammer “S2.2”](#technical-details-on-low-power-jammer-s22)

[Technical details on low-power jammer “S2.3”](#technical-details-on-low-power-jammer-s23)

[Technical details on low-power jammer “S2.4”](#technical-details-on-low-power-jammer-s24)

[Technical details on low-power jammer “U1.1 to U1.4”](#technical-details-on-low-power-jammer-u11-to-u14)

[Technical details on low-power jammer “H1.1”](#technical-details-on-low-power-jammer-h11)

[Technical details on low-power jammer “H1.2”](#technical-details-on-low-power-jammer-h12)

[Technical details on low-power jammer “H1.3”](#technical-details-on-low-power-jammer-h13)

[Technical details on low-power jammer “H1.4”](#technical-details-on-low-power-jammer-h14)

[Technical details on low-power jammer “H1.5”](#technical-details-on-low-power-jammer-h15)

[Technical details on low-power jammer “H2.1 and H2.2”](#technical-details-on-low-power-jammer-h21-and-h22)

[Technical details on low-power jammer “H3.1”](#technical-details-on-low-power-jammer-h31)

[Technical details on low-power jammer “H3.2”](#technical-details-on-low-power-jammer-h32)

[Technical details on low-power jammer “H3.3”](#technical-details-on-low-power-jammer-h33)

[Technical details on low-power jammer "H4.1"](#technical-details-on-low-power-jammer-h41)

[Technical details on low-power jammer “H6.1”](#technical-details-on-low-power-jammer-h61)

[Technical details on low-power jammer “H6.2”](#technical-details-on-low-power-jammer-h62)

[Technical details on low-power jammer “H6.3”](#technical-details-on-low-power-jammer-h63)

[Technical details on low-power jammer “H6.4”](#technical-details-on-low-power-jammer-h64)

[Technical details on low-power jammer “H6.5”](#technical-details-on-low-power-jammer-h65)

[Technical details on low-power jammer “H6.6”](#technical-details-on-low-power-jammer-h66)

[Technical details on low-power jammer “F6.1”](#technical-details-on-low-power-jammer-f61)

[Technical details on low-power jammer "H8.1"](#technical-details-on-low-power-jammer-h81)

[Technical details on the meaconing setup “Porcellum” / “F1.1”](#technical-details-on-the-meaconing-setup-porcellum--f11)

[Technical details on the high-power jammer “Porcus Major”/ “F8.1”](#technical-details-on-the-high-power-jammer-porcus-major-f81)

[Technical details on software defined radio mobile SDR spoofer “F1.2”](#technical-details-on-software-defined-radio-mobile-sdr-spoofer-f12)

## Appendix G - Technical details on jammer equipment

The nomenclature for naming of the jammer equipment is as follows:

| **1<sup>st</sup> Letter (Norwegian / English)**     | **1<sup>St</sup> digit** | **2<sup>nd</sup> digit**           |
|-----------------------------------------------------|--------------------------|------------------------------------|
| **S** = Sigarett / Cigarette                        | **Number of antennas**   | **\# jammer within same category** |
| **H** = Håndholdt / Handheld                        |                          |                                    |
| **U** = USB / USB stick                             |                          |                                    |
| **F** = Fastmontert / Permanently installed (Fixed) |                          |                                    |

Exempli gratia:

S1.2, is a cigarette type jammer, that has 1 antenna, and is unit nr.2
in this category.

Additional information:

-   Each chapter gives an overview of each jammer brought to Jammertest.
    As far as possible, it gives information on

    -   Centre frequency \[MHz\]

    -   Bandwidth \[MHz\]

    -   Power Spectral Density (PSD) \[dBm/MHz\] for the entire
        bandwidth

    -   Total output power (TX total) \[dBm\] for the entire bandwidth

    -   CF max \[dBm\] (maxhold power at the centre frequency)

    -   Sweep rate \[µs\] (if applicable)

    -   Modulation

-   Indicators such as “L1, L2, L5” etc. are used to indicate main bands
    of attack, used for convenience to distinguish between jammers’
    modus operandi

-   2023 measurements

    -   Technical details on low power jammers given in this appendix
        are from uncalibrated measurements. They are rough estimates
        given for both the frequency and time domain. Power levels are
        not correctly displayed on the chart, because of external
        attenuators used during measurements with a signal analyser.
        There may also have been some constraints in the measurement
        device, causing fast frequency components to not be correctly
        displayed.

-   2024 measurements

    -   Measurements done with a R&S FSW. All measurements were
        performed connected directly to the jammers’ antenna port, with
        the other antennas disconnected and (if applicable) DIP switches
        for the other antenna ports disabled. Powe levels etc. should be
        as close to reality as possible for output power at the antenna
        port.

    -   Throughout the measurements, bandwidth is defined as 3 dB from
        local (identifiable) maxima along the maxhold’s descent.

    -   TX power is measured within said bandwidth. Note that TX total
        is measured over the entire bandwidth, so that peak output power
        is not equal to TX total.

### Technical details on low-power jammer “S1.1”
<img src="media\image1.jpeg" style="width:3.08264in;height:2.3125in" />

The jammer S1.1 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S1.1 is an one-antenna, so-called “L1-only”, jammer, disrupting only the
upper L-band.

<u>Technical characteristics of S1.1 (2024 measurements)</u>

| Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| 1577,40                  | 29,96             | 7,58            | 22,34            | 7,89           | 37,1              | Sawtooth   |

<img src="media\image2.png" style="width:6.27083in;height:4.16667in" />

G 1: Frequency and power measurement of jammer S1.1

<img src="media\image3.png" style="width:6.27083in;height:4.16667in" />

G 2: Real-time persistence and spectrogram measurement of jammer S1.1

<img src="media\image4.png" style="width:6.27083in;height:4.16667in" />

G 3: Time domain (analog demod) measurement of jammer S1.1

### Technical details on low-power jammer “S1.2”
<img src="media\image1.jpeg" style="width:3.08264in;height:2.3125in" />

The jammer S1.2 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S1.2 is an one-antenna, so-called “L1-only”, jammer, disrupting only the
upper L-band.

<u>Technical characteristics of S1.2 (2024 measurements)</u>

| Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| 1582,56                  | 40,03             | 12,38           | 29,01            | 12,61          | 21,56             | Sawtooth   |

<img src="media\image5.png" style="width:6.26806in;height:4.16458in" alt="Et bilde som inneholder tekst, skjermbilde, line, Plottdiagram Automatisk generert beskrivelse" />

G 4: Frequency and power measurement of jammer S1.2

<img src="media\image6.png" style="width:6.27083in;height:4.16667in" />

G 5: Real-time persistence and spectrogram measurement of jammer S1.2

<img src="media\image7.png" style="width:6.27083in;height:4.16667in" />

G 6: Time domain (analog demod) measurement of jammer S1.2

### Technical details on low-power jammer “S1.3”
<img src="media\image1.jpeg" style="width:3.08264in;height:2.3125in" />

The jammer S1.3 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S1.3 is an one-antenna, so-called “L1-only”, jammer, disrupting only the
upper L-band.

<u>Technical characteristics of S1.3 (2024 measurements)</u>

| Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| 1579,63                  | 31,88             | 7,56            | 22,60            | 7,93           | 37,5              | Sawtooth   |

<img src="media\image8.png" style="width:6.27083in;height:4.16667in" />

G 7: Frequency and power measurement of jammer S1.3

<img src="media\image9.png" style="width:6.27083in;height:4.16667in" />

G 8: Real-time persistence and spectrogram measurement of jammer S1.3

<img src="media\image10.png" style="width:6.27083in;height:4.16667in" />

G 9: Time domain (analog demod) measurement of jammer S1.3

### Technical details on low-power jammer “S2.1” 
<img src="media\image11.png" style="width:3.05556in;height:2.29167in" />

The jammer S2.1 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S2.1 is a two-antenna, so-called “L1+L2”, jammer, disrupting both the
upper and lower L-band.

<u>Technical characteristics of S2.1 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation     |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|----------------|
| “L1”    | 1581,59                  | 85,41             | 13,36           | 32,68            | 16,64          | 40,63             | Sawtooth+burst |
| “L2”    | 1198,05                  | 96,58             | 13,92           | 33,75            | 17,30          | 42,1              | Sawtooth+burst |

<img src="media\image12.png" style="width:6.27083in;height:4.16667in" />

G 10: Frequency and power measurement of jammer S2.1 on antenna “L1”

<img src="media\image13.png" style="width:6.27083in;height:4.16667in" />

G 11: Frequency and power measurement of jammer S2.1 on antenna “L2"

<img src="media\image14.png" style="width:6.27083in;height:4.16667in" />

G 12: Real-time persistence and spectrogram measurement of jammer S2.1
on antenna "L1"

<img src="media\image15.png" style="width:6.27083in;height:4.16667in" />

G 13: Real-time persistence and spectrogram measurement of jammer S2.1
on antenna "L2"

<img src="media\image16.png" style="width:6.27083in;height:4.16667in" />

G 14: Time domain (analog demod) measurement of jammer S2.1 on antenna
“L1”

<img src="media\image17.png" style="width:6.27083in;height:4.16667in" />

G 15: Time domain (analog demod) measurement with wider span of jammer
S2.1 on antenna “L1”

<img src="media\image18.png" style="width:6.27083in;height:4.16667in" />

G 16: Time domain (analog demod) measurement of jammer S2.1 on antenna
“L2”

### Technical details on low-power jammer “S2.2” 
<img src="media\image11.png" style="width:3.05556in;height:2.29167in" />

The jammer S2.2 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S2.2 is a two-antenna, so-called “L1+L2”, jammer, disrupting both the
upper and lower L-band.

<u>Technical characteristics of S2.2 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation     |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|----------------|
| “L1”    | 1580,86                  | 87,69             | 12,82           | 32,25            | 16,17          | 40,7              | Sawtooth+burst |
| “L2”    | 1207,55                  | 102,04            | 11,95           | 32,04            | 17,02          | 41,0              | Sawtooth+burst |

<img src="media\image19.png" style="width:6.26806in;height:4.16482in" alt="Et bilde som inneholder tekst, skjermbilde, Plottdiagram, nummer Automatisk generert beskrivelse" />

G 17: Frequency and power measurement of jammer S2.2 on antenna “L1”

<img src="media\image20.png" style="width:6.27083in;height:4.16667in" />

G 18: Frequency and power measurement of jammer S2.2 on antenna “L2"

<img src="media\image21.png" style="width:6.27083in;height:4.16667in" />

G 19: Real-time persistence and spectrogram measurement of jammer S2.2
on antenna "L1"

<img src="media\image22.png" style="width:6.27083in;height:4.16667in" />

G 20: Real-time persistence and spectrogram measurement of jammer S2.2
on antenna "L2"

<img src="media\image23.png" style="width:6.27083in;height:4.16667in" />

G 21: Time domain (analog demod) measurement of jammer S2.2 on antenna
“L1”

<img src="media\image24.png" style="width:6.27083in;height:4.16667in" />

G 22: Time domain (analog demod) measurement of jammer S2.2 on antenna
“L2”

### Technical details on low-power jammer “S2.3” 
<img src="media\image11.png" style="width:3.05556in;height:2.29167in" />

The jammer S2.3 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S2.3 is a two-antenna, so-called “L1+L2”, jammer, disrupting both the
upper and lower L-band.

<u>Technical characteristics of S2.3 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation     |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|----------------|
| “L1”    | 1586,65                  | 93,19             | 14,30           | 34,0             | 17,40          | 46,7              | Sawtooth+burst |
| “L2”    | 1204,33                  | 102,05            | 12,01           | 32,1             | 17,06          | 50,5              | Sawtooth+burst |

<img src="media\image25.png" style="width:6.27083in;height:4.16667in" />

G 23: Frequency and power measurement of jammer S2.3 on antenna “L1”

<img src="media\image26.png" style="width:6.27083in;height:4.16667in" />

G 24: Frequency and power measurement of jammer S2.3 on antenna “L2"

<img src="media\image27.png" style="width:6.27083in;height:4.16667in" />

G 25: Real-time persistence and spectrogram measurement of jammer S2.3
on antenna "L1"

<img src="media\image28.png" style="width:6.27083in;height:4.16667in" />

G 26: Real-time persistence and spectrogram measurement of jammer S2.3
on antenna "L2"

<img src="media\image29.png" style="width:6.27083in;height:4.16667in" />

G 27: Time domain (analog demod) measurement of jammer S2.3 on antenna
“L1”

<img src="media\image30.png" style="width:6.27083in;height:4.16667in" />

G 28: Time domain (analog demod) measurement of jammer S2.3 on antenna
“L2”

### Technical details on low-power jammer “S2.4” 
<img src="media\image11.png" style="width:3.05556in;height:2.29167in" />

The jammer S2.4 belongs to the ‘Cigarette jammer’ category of jammers.
Such jammers are often installed in the cigarette lighter outlet in
cars. They are intended to cover the car, and a given radius around the
car.

S2.4 is a two-antenna, so-called “L1+L2”, jammer, disrupting both the
upper and lower L-band.

<u>Technical characteristics of S2.4 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation     |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|----------------|
| “L1”    | 1582,09                  | 86,35             | 12,42           | 31,78            | 15,91          | 43,5              | Sawtooth+burst |
| “L2”    | 1202,90                  | 96,56             | 13,63           | 33,48            | 17,03          | 47,3              | Sawtooth+burst |

<img src="media\image31.png" style="width:6.27083in;height:4.16667in" />

G 29: Frequency and power measurement of jammer S2.4 on antenna “L1”

<img src="media\image32.png" style="width:6.27083in;height:4.16667in" />

G 30: Frequency and power measurement of jammer S2.4 on antenna “L2"

<img src="media\image33.png" style="width:6.27083in;height:4.16667in" />

G 31: Real-time persistence and spectrogram measurement of jammer S2.4
on antenna "L1"

<img src="media\image34.png" style="width:6.27083in;height:4.16667in" />

G 32: Real-time persistence and spectrogram measurement of jammer S2.4
on antenna "L2"

<img src="media\image35.png" style="width:6.27083in;height:4.16667in" />

G 33: Time domain (analog demod) measurement of jammer S2.4 on antenna
“L1”

<img src="media\image36.png" style="width:6.27083in;height:4.16667in" />

G 34: Time domain (analog demod) measurement of jammer S2.4 on antenna
“L2”

### Technical details on low-power jammer “U1.1 to U1.4”
<img src="media\image37.png" style="width:2.75in;height:2.0625in" />

USB jammers is category of jammers that is often installed in the USB
outlet. The are intended to cover a small radius. These particular
jammers suggest in the LED screen that they jam two bands, although this
is not the case (see below).

<u>Technical characteristics of U1.1 to U1.4 (2023 measurements)</u>

| Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| 1590 - 1600              | 70 - 80           | N/A             | N/A              | N/A            | 5 - 8             | Sawtooth   |

<img src="media\image38.png" style="width:6.41111in;height:4.25764in" alt="Et bilde som inneholder tekst, skjermbilde, line, nummer Automatisk generert beskrivelse" />

G 35: Example measurement of a U1.1 – U1.4 jammer

**  
**

### Technical details on low-power jammer “H1.1”

<img src="media\image39.jpeg" style="width:1.97014in;height:2.62431in" />The
jammer H1.1 belongs to the ‘Handheld category’ of jammers. It is a
medium weight battery driven jammer with a configuration panel for
operation: multi-frequency and multi-modulation for both low and high
output power. Its commercially available for military training purposes
as Novatel’s NEAT-jammer. Antenna has TNC-connector.

H1.1 is an one-antenna, yet multi-frequency, jammer, therefore a
so-called “L1+L2”, disrupting parts of both the upper and lower L-band.

Configuration choices are (as provided by the producer):

-   Centre frequency: 1575.42 MHz and 1227.6 MHz

-   Estimated output power: low power -5 dBm, high power 20 dBm

-   Type of modulation: narrow band (NB), wide band (WB), continuous
    wave (CW), chirp/sweep and other (optional to program)

In the 2024 measurements below, bandwidth is defined as

-   main lobe in PRN signal

-   3 dB from local (identifiable) maxima

<u>Technical characteristics of H1.1 (2024 measurements)</u>

| Antenna configuration | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation                     |
|-----------------------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|--------------------------------|
| L1, NB, HIGH PWR      | 1575,42                  | 2,05              | 17,52           | 20,63            | 11,07          | N/A               | PRN (spreading code of 1 MHz)  |
| L1, WB, HIGH PWR      | 1575,40                  | 20,03             | 8,20            | 21,25            | 11,43          | N/A               | PRN (spreading code of 10 MHz) |
| L1, CW, HIGH PWR      | 1575,42                  | 0,103             | 22,50           | 12,62            | 13,67          | N/A               | CW                             |
| L1, CHIRP, HIGH PWR   | 1575,60                  | 18,75             | 3,10            | 15,83            | -5,73          | 10,42             | Sawtooth                       |
| L1, NB, LOW PWR       | 1575,42                  | 2,05              | -12,84          | -9,73            | -19,35         | N/A               | PRN (spreading code of 1 MHz)  |
| L1, WB, LOW PWR       | 1575,40                  | 19,93             | -21,66          | -8,66            | -17,91         | N/A               | PRN (spreading code of 10 MHz) |
| L1, CW, LOW PWR       | 1575,42                  | 0,10              | -7,55           | -17,46           | -16,37         | N/A               | CW                             |
| L1, CHIRP, LOW PWR    | 1575,60                  | 18,75             | -27,03          | -14,31           | -35,65         | 10,46             | Sawtooth                       |
| L2, NB, HIGH PWR      | 1227,42                  | 2,049             | 18,73           | 21,84            | 12,17          | N/A               | PRN (spreading code of 1 MHz)  |
| L2, WB, HIGH PWR      | 1227,36                  | 20,30             | 9,27            | 22,34            | 12,09          | N/A               | PRN (spreading code of 10 MHz) |
| L2, CW, HIGH PWR      | 1227,42                  | 0,10              | 23,96           | 14,13            | 15,17          | N/A               | CW                             |
| L2, CHIRP, HIGH PWR   | 1227,22                  | 18,79             | 4,98            | 17,72            | -4,11          | 10,4              | Sawtooth                       |
| L2, NB, LOW PWR       | 1227,42                  | 2,05              | -11,20          | -8,09            | -17,79         | N/A               | PRN (spreading code of 1 MHz)  |
| L2, WB, LOW PWR       | 1227,36                  | 20,30             | -20,39          | -7,32            | -17,41         | N/A               | PRN (spreading code of 10 MHz) |
| L2, CW, LOW PWR       | 1227,42                  | 0,10              | -5,98           | -15,81           | -14,77         | N/A               | CW                             |
| L2, CHIRP, LOW PWR    | 1227,22                  | 18,76             | -24,97          | -12,23           | -33,98         | 10,4              | Sawtooth                       |

Measurements given below are for ‘High power’ configurations only.

<img src="media\image40.png" style="width:6.27083in;height:4.16667in" />

G 36: Frequency and power measurement of jammer H1.1 with antenna
configuration L1 Narrow band High Power (NB HIGH PWR)

<img src="media\image41.png" style="width:6.27083in;height:4.16667in" />

G 37: Frequency and power measurement of jammer H1.1 with antenna
configuration L1 Wide band High Power (WB HIGH PWR)

<img src="media\image42.png" style="width:6.27083in;height:4.16667in" />

G 38: Frequency and power measurement of jammer H1.1 with antenna
configuration L1 Continuous Wave band High Power (CW HIGH PWR)

<img src="media\image43.png" style="width:6.27083in;height:4.16667in" />

G 39: Frequency and power measurement of jammer H1.1 with antenna
configuration L1 Chirp High Power (CHIRP HIGH PWR)

<img src="media\image44.png" style="width:6.26806in;height:4.16482in" alt="Et bilde som inneholder tekst, skjermbilde, Fargerikt, Plottdiagram Automatisk generert beskrivelse" />

G 40: Real-time persistence and spectrogram measurement of jammer H1.1
with antenna configuration L1 Narrow band High Power (NB HIGH PWR)

<img src="media\image45.png" style="width:6.27083in;height:4.16667in" />

G 41: Real-time persistence and spectrogram measurement with wider span
of jammer H1.1 with antenna configuration L1 Narrow band High Power (NB
HIGH
PWR)<img src="media\image46.png" style="width:6.27083in;height:4.16667in" />

G 42: Real-time persistence and spectrogram measurement of jammer H1.1
with antenna configuration L1 Wide band High Power (WB HIGH PWR)

<img src="media\image47.png" style="width:6.27083in;height:4.16667in" />

G 43: Real-time persistence and spectrogram measurement with wider span
of jammer H1.1 with antenna configuration L1 Wide band High Power (WB
HIGH PWR)

<img src="media\image48.png" style="width:6.27083in;height:4.16667in" />

G 44: Real-time persistence and spectrogram measurement with wider span
of jammer H1.1 with antenna configuration L1 Continuous Wave band High
Power (CW HIGH PWR)

<img src="media\image49.png" style="width:6.27083in;height:4.16667in" />

G 45: Real-time persistence and spectrogram measurement of jammer H1.1
with antenna configuration L1 Chirp High Power (CHIRP HIGH PWR)

<img src="media\image50.png" style="width:6.27083in;height:4.16667in" />

G 46: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L1 Narrow band High Power (NB HIGH PWR)

<img src="media\image51.png" style="width:6.27083in;height:4.16667in" />

G 47: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L1 Wide band High Power (WB HIGH PWR)

<img src="media\image52.png" style="width:6.27083in;height:4.16667in" />

G 48: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L1 Continuous Wave band High Power (CW HIGH PWR)

<img src="media\image53.png" style="width:6.27083in;height:4.16667in" />

G 49: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L1 Chirp High Power (CHIRP HIGH PWR)

<img src="media\image54.png" style="width:6.27083in;height:4.16667in" />

G 50: Frequency and power measurement of jammer H1.1 with antenna
configuration L2 Narrow band High Power (NB HIGH PWR)

<img src="media\image55.png" style="width:6.27083in;height:4.16667in" />

G 51: Frequency and power measurement of jammer H1.1 with antenna
configuration L2 Wide band High Power (WB HIGH PWR)

<img src="media\image56.png" style="width:6.27083in;height:4.16667in" />

G 52: Frequency and power measurement of jammer H1.1 with antenna
configuration L2 Continuous Wave band High Power (CW HIGH PWR)

<img src="media\image57.png" style="width:6.26806in;height:4.16482in" alt="Et bilde som inneholder tekst, skjermbilde, Plottdiagram, line Automatisk generert beskrivelse" />

G 53: Frequency and power measurement of jammer H1.1 with antenna
configuration L2 Chirp High Power (CHIRP HIGH PWR)

<img src="media\image58.png" style="width:6.26806in;height:4.16482in" alt="Et bilde som inneholder tekst, skjermbilde, Fargerikt, Plottdiagram Automatisk generert beskrivelse" />

G 54: Real-time persistence and spectrogram measurement of jammer H1.1
with antenna configuration L2 Narrow band High Power (NB HIGH PWR)

<img src="media\image59.png" style="width:6.26806in;height:4.16482in" alt="Et bilde som inneholder tekst, skjermbilde, Plottdiagram, line Automatisk generert beskrivelse" />

G 55: Real-time persistence and spectrogram measurement with wider span
of jammer H1.1 with antenna configuration L2 Narrow band High Power (NB
HIGH PWR)

<img src="media\image60.png" style="width:6.27083in;height:4.16667in" />

G 56: Real-time persistence and spectrogram measurement of jammer H1.1
with antenna configuration L2 Wide band High Power (WB HIGH PWR)

<img src="media\image61.png" style="width:6.26806in;height:4.16482in" />

G 57: Real-time persistence and spectrogram measurement with wider span
of jammer H1.1 with antenna configuration L2 Wide band High Power (WB
HIGH PWR)

<img src="media\image62.png" style="width:6.27083in;height:4.16667in" />

G 58: Real-time persistence and spectrogram measurement with wider span
of jammer H1.1 with antenna configuration L2 Continuous Wave band High
Power (CW HIGH PWR)

<img src="media\image63.png" style="width:6.27083in;height:4.16667in" />

G 59: Real-time persistence and spectrogram measurement of jammer H1.1
with antenna configuration L2 Chirp High Power (CHIRP HIGH PWR)

<img src="media\image64.png" style="width:6.27083in;height:4.16667in" />

G 60: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L2 Narrow band High Power (NB HIGH PWR)

<img src="media\image65.png" style="width:6.27083in;height:4.16667in" />

G 61: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L2 Wide band High Power (WB HIGH PWR)

<img src="media\image66.png" style="width:6.27083in;height:4.16667in" />

G 62: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L2 Continuous Wave band High Power (CW HIGH PWR)

<img src="media\image67.png" style="width:6.27083in;height:4.16667in" />

G 63: Time domain (analog demod) measurement of jammer H1.1 with antenna
configuration L2 Chirp High Power (CHIRP HIGH PWR)

### Technical details on low-power jammer “H1.2”
<img src="media\image68.jpeg" style="width:1.86847in;height:2.49414in" />

The jammer H1.2 belongs to the ‘Handheld category’ of jammers. It is a
small and light battery driven jammer with an easy operation, just an
on/off-button with a LED-light to indicate activation.

H1.2 is an one-antenna, so-called “L1-only”, jammer, disrupting only the
upper L-band.

<u>Technical characteristics of H1.2 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “L1”    | 1575,22                  | 21,99             | 14,35           | 27,78            | 9,36           | 6,08              | Sawtooth   |

<img src="media\image69.png" style="width:6.27083in;height:4.16667in" />

G 64: Frequency and power measurement of jammer H1.2

<img src="media\image70.png" style="width:6.26806in;height:4.16482in" />

G 65: Real-time persistence and spectrogram measurement of jammer H1.2

<img src="media\image71.png" style="width:6.27083in;height:4.16667in" />

G 66: Time domain (analog demod) measurement of jammer H1.2

### Technical details on low-power jammer “H1.3”
<img src="media\image72.png" style="width:0.82222in;height:2.26042in" />

H1.3 is a small, handheld and battery driven jammer using frequency
hopping (normally commercially available jammers employ chirp signals,
making this jammer an oddity).

H1.3 is an one-antenna, so-called “L1-only”, jammer, disrupting only the
upper L-band.

<u>Technical characteristics of H1.3 (2023 measurements)</u>

| Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation        |
|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|-------------------|
| 1575                     | 1                 | N/A             | N/A              | N/A            | 5 - 8             | Frequency hopping |

-   Type of modulation: frequency hopping

    -   Jumping between 6 separated frequencies. Every 50 ms the
        frequency increases 200 kHz, starting with 1574.62 MHz. After
        approximately 1 MHz the frequency jumps back to the start
        frequency at 1574.62 MHz.

<img src="media\image73.png" style="width:5.91983in;height:2.01707in" alt="Et bilde som inneholder tekst, skjermbilde, line, nummer Automatisk generert beskrivelse" />

<img src="media\image74.png" style="width:5.93948in;height:1.55824in" />

G 67: Example measurement of H1.3 jammer

### Technical details on low-power jammer “H1.4”

Jammer H1.4 is assumed more or less identical to jammer H1.1
(originating from the same source and built by the same producer).

### Technical details on low-power jammer “H1.5”

Jammer H1.5 is assumed more or less identical to jammer H1.1
(originating from the same source and built by the same producer).

### Technical details on low-power jammer “H2.1 and H2.2”
<img src="media\image75.png" style="width:2.1875in;height:2.33958in" />

H2.1 and H2.2 are small and light handheld, battery driven jammers with
built-in antennas.

They are two-antenna, so-called “L1+L2”, jammers, disrupting both the
upper and lower L-band.

<u>Technical characteristics of H2.1 and H2.2 (2023 measurements)</u>

| Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| 1580                     | 20                | N/A             | N/A              | N/A            | 9                 | Sawtooth   |
| 1227                     | 20                | N/A             | N/A              | N/A            | 9                 | Sawtooth   |

<img src="media\image76.png" style="width:6.35177in;height:3.76045in" alt="Et bilde som inneholder tekst, skjermbilde, line, programvare Automatisk generert beskrivelse" />

G 68: Example measurement of H2.1 and H2.2 jammer

### Technical details on low-power jammer “H3.1”
<img src="media\image77.jpeg" style="width:2.29167in;height:3.05625in" />

The jammer H3.1 belongs to the ‘Handheld category’ of jammers. It is a
small and light battery driven jammer with an easy operation, just an
on/off-button with a LED-light to indicate activation.

H3.1 is a three-antenna, so-called “multi-frequency”, jammer, but not a
“multi-GNSS-jammer”. It jams three different bands, but only one channel
is relevant for GNSS bands (“L1-only”), so disrupting only the upper
L-band.

Relevant GNSS antenna is marked: “GPS”

<u>Technical characteristics of H3.1 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “GPS”   | 1577,93                  | 28,29             | 17,34           | 31,86            | 16,17          | 6,16              | Sawtooth   |

<img src="media\image78.png" style="width:6.27083in;height:4.16667in" />

*G* *69: Frequency and power measurement of jammer H3.1 on antenna
“GPS”*

<img src="media\image79.png" style="width:6.27083in;height:4.16667in" />

G 70: Real-time persistence and spectrogram measurement of jammer H3.1
on antenna “GPS”

<img src="media\image80.png" style="width:6.27083in;height:4.16667in" />

G 71: Time domain (analog demod) measurement of jammer H3.1 on antenna
“GPS”

### Technical details on low-power jammer “H3.2”
<img src="media\image77.jpeg" style="width:2.29167in;height:3.05625in" />

The jammer H3.2 belongs to the ‘Handheld category’ of jammers. It is a
small and light battery driven jammer with an easy operation, just an
on/off-button with a LED-light to indicate activation.

H3.2 is a three-antenna, so-called “multi-frequency”, jammer, but not a
“multi-GNSS-jammer”. It jams three different bands, but only one channel
is relevant for GNSS bands (“L1-only”), so disrupting only the upper
L-band.

Relevant GNSS antenna is marked: “GPS”

<u>Technical characteristics of H3.2 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “GPS”   | 1579,52                  | 30,81             | 17,97           | 32,86            | 16,65          | 6,44              | Sawtooth   |

<img src="media\image81.png" style="width:6.27083in;height:4.16667in" />

G 72: Frequency and power measurement of jammer H3.2 on antenna “GPS”

<img src="media\image82.png" style="width:6.27083in;height:4.16667in" />

G 73: Real-time persistence and spectrogram measurement of jammer H3.2
on antenna “GPS”

<img src="media\image83.png" style="width:6.27083in;height:4.16667in" />

G 74: Time domain (analog demod) measurement of jammer H3.2 on antenna
“GPS”

### Technical details on low-power jammer “H3.3”
<img src="media\image84.png" style="width:1.32292in;height:2.91667in" />

The jammer H3.3 belongs to the ‘Handheld category’ of jammers. It is a
small and relatively light battery driven jammer with an easy operation,
just an on/off-button with a LED-light to indicate activation.

H3.3 is a three-antenna, so-called “L1+L2+L5”, jammer, disrupting both
the upper and lower L-band.

The three antennas are marked with white lines of different length:
short=L1, medium=L2, long=L5

The jammer has additional noise in several other (non GNSS) frequency
bands, but with significant lower power.

<u>Technical characteristics of H3.3 (2024 measurements)</u>

| Antenna       | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|---------------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “short” (L1)  | 1575,35                  | 19,93             | 26,37           | 39,36            | 23,56          | 12,96             | Sawtooth   |
| “medium” (L2) | 1228,06                  | 14,36             | 27,38           | 38,95            | 22,44          | 12,51             | Sawtooth   |
| “long” (L5)   | 1176,24                  | 17,45             | 28,62           | 41,04            | 25,83          | 12,51             | Sawtooth   |

<img src="media\image85.png" style="width:6.27083in;height:4.16667in" />

G 75: Frequency and power measurement of jammer H3.3 on antenna “short”
(L1)

<img src="media\image86.png" style="width:6.27083in;height:4.16667in" />

G 76: Frequency and power measurement of jammer H3.3 on antenna “medium”
(L2)

<img src="media\image87.png" style="width:6.27083in;height:4.16667in" />

G 77: Frequency and power measurement of jammer H3.3 on antenna “long”
(L5)

<img src="media\image88.png" style="width:6.27083in;height:4.16667in" />

G 78: Real-time persistence and spectrogram measurement of jammer H3.3
on antenna “short” (L1)

<img src="media\image89.png" style="width:6.27083in;height:4.16667in" />

G 79: Real-time persistence and spectrogram measurement of jammer H3.3
on antenna “medium” (L2)

<img src="media\image90.png" style="width:6.27083in;height:4.16667in" />

G 80: Real-time persistence and spectrogram measurement of jammer H3.3
on antenna “long” (L5)

<img src="media\image91.png" style="width:6.27083in;height:4.16667in" />

G 81: Time domain (analog demod) measurement of jammer H3.3 on antenna
“short” (L1)

<img src="media\image92.png" style="width:6.27083in;height:4.16667in" />

G 82: Time domain (analog demod) measurement of jammer H3.3 on antenna
“medium” (L2)

<img src="media\image93.png" style="width:6.27083in;height:4.16667in" />

G 83: Time domain (analog demod) measurement of jammer H3.3 on antenna
“long” (L5)

### Technical details on low-power jammer H4.1
<img src="media\image94.png" style="width:2.03056in;height:3.09306in" />

The jammer H4.1 belongs to the ‘Handheld category’ of jammers. It is a
small and relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H4.1 is a four-antenna, so-called “L1+L2+L5+E6”, jammer, disrupting both
the upper and lower L-band.

The four antennas are marked with numbers: “1” (L1), “2” (E6), “3” (L2)
and “4” (L5)

The jammer has additional noise (harmonics) in several other (non GNSS)
frequency bands.

<u>Technical characteristics of H4.1 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation         |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|--------------------|
| “1” (L1) | 1548,02                  | 102,67            | 21,14           | 41,25            | 25,20          | 8,82              | Sawtooth-modulated |
| “2” (E6) | 1261,92                  | 48,80             | 22,38           | 39,26            | 22,33          | 8,86              | Sawtooth           |
| “3” (L2) | 1220,34                  | 47,88             | 21,08           | 37,88            | 20,29          | 8,82              | Sawtooth           |
| “4” (L5) | 1182,32                  | 39,66             | 22,87           | 38,85            | 22,83          | 8,84              | Sawtooth           |

<img src="media\image95.png" style="width:6.27083in;height:4.40625in" />

G 84: Frequency and power measurement of jammer H4.1 on antenna “1”
(L1)

<img src="media\image96.png" style="width:6.27083in;height:4.26042in" />

G 85: Frequency and power measurement with wider span of jammer H4.1 on
antenna “1” (L1)

<img src="media\image97.png" style="width:6.27083in;height:4.40625in" />

G 86: Frequency and power measurement of jammer H4.1 on antenna “2” (E6)

<img src="media\image98.png" style="width:6.27083in;height:4.40625in" />

G 87: Frequency and power measurement with wider span of jammer H4.1 on
antenna “2” (E6)

<img src="media\image99.png" style="width:6.27083in;height:4.40625in" />

G 88: Frequency and power measurement of jammer H4.1 on antenna “3” (L2)

<img src="media\image100.png" style="width:6.27083in;height:4.40625in" />

G 89: Frequency and power measurement with wider span of jammer H4.1 on
antenna “3” (L2)

<img src="media\image101.png" style="width:6.27083in;height:4.40625in" />

G 90: Frequency and power measurement of jammer H4.1 on antenna “4” (L5)

<img src="media\image102.png" style="width:6.27083in;height:4.40625in" />

G 91: Frequency and power measurement with wider span of jammer H4.1 on
antenna “4” (L5)

<img src="media\image103.png" style="width:6.27083in;height:4.40625in" />

G 92: Real-time persistence and spectrogram measurement of jammer H4.1
on antenna “1” (L1)

<img src="media\image104.png" style="width:6.27083in;height:4.40625in" />

G 93: Real-time persistence and spectrogram measurement of jammer H4.1
on antenna “2” (E6)

<img src="media\image105.png" style="width:6.27083in;height:4.40625in" />

G 94: Real-time persistence and spectrogram measurement of jammer H4.1
on antenna “3” (L2)

<img src="media\image106.png" style="width:6.27083in;height:4.40625in" />

G 95: Real-time persistence and spectrogram measurement of jammer H4.1
on antenna “4” (L5)

<img src="media\image107.png" style="width:6.27083in;height:4.40625in" />

G 96: Time domain (analog demod) measurement of jammer H4.1 on antenna
“1” (L1)

<img src="media\image108.png" style="width:6.27083in;height:4.40625in" />

G 97: Time domain (analog demod) measurement of jammer H4.1 on antenna
“2” (E6)

<img src="media\image109.png" style="width:6.27083in;height:4.40625in" />

G 98: Time domain (analog demod) measurement of jammer H4.1 on antenna
“3” (L2)

<img src="media\image110.png" style="width:6.27083in;height:4.40625in" />

G 99: Time domain (analog demod) measurement of jammer H4.1 on antenna
“4” (L5)

### Technical details on low-power jammer “H6.1”
<img src="media\image111.jpeg" style="width:2.27083in;height:2.45in" />

The jammer H6.1 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H6.1 is a six-antenna, so-called “multi-frequency”, jammer, but
technically not a “multi-GNSS-jammer”. It jams six different bands, but
only two channels are relevant for GNSS bands, both in the upper L-band
(so “L1-only”), thus only disrupting the upper L-band.

The most relevant GNSS antenna is marked “6”. The periphery antenna is
marked “4”. To avoid disrupting non-GNSS services, use only antenna “6”.

<u>Technical characteristics of H6.1 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “4”      | 1621,23                  | 87,50             | 2,89            | 22,31            | 5,57           | 5,9               | Sawtooth   |
| “6” (L1) | 1581,18                  | 22,24             | 24,60           | 38,07            | 24,37          | 5,86              | Sawtooth   |

<img src="media\image112.png" style="width:6.27083in;height:4.16667in" />

G 100: Frequency and power measurement of jammer H6.1 on antenna “6”
(L1)

<img src="media\image113.png" style="width:6.27083in;height:4.16667in" />

G 101: Frequency and power measurement of jammer H6.1 on antenna “4”

<img src="media\image114.png" style="width:6.27083in;height:4.16667in" />

G 102: Real-time persistence and spectrogram measurement of jammer H6.1
on antenna “6” (L1)

<img src="media\image115.png" style="width:6.27083in;height:4.16667in" />

G 103: Real-time persistence and spectrogram measurement of jammer H6.1
on antenna “4”

<img src="media\image116.png" style="width:6.27083in;height:4.16667in" />

G 104: Time domain (analog demod) measurement of jammer H6.1 on antenna
“6” (L1)

<img src="media\image117.png" style="width:6.27083in;height:4.16667in" />

G 105: Time domain (analog demod) measurement of jammer H6.1 on antenna
“4”

### Technical details on low-power jammer “H6.2”
<img src="media\image118.jpeg" style="width:1.98056in;height:2.1375in" />

The jammer H6.2 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H6.2 is a six-antenna, so-called “multi-frequency”, jammer. It jams six
different bands, but only three channels are relevant for GNSS bands
(“L1+L2+L5”), thus disrupting the upper and lower L-band.

The relevant antennas are marked with numbers: “4” (L1), “5” (L5) and
“6” (L2).

The jammer has additional noise in several other (non GNSS) frequency
bands, but with significant lower power.

<u>Technical characteristics of H6.2 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation                    |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|-------------------------------|
| “4” (L1) | 1581,51                  | 30,00             | 26,50           | 41,27            | 25,99          | 7,0 / 28,2        | Sawtooth modulated unto sinus |
| “5” (L5) | 1154,62                  | 110,77            | 19,98           | 40,42            | 24,57          | 7,14              | Sawtooth                      |
| “6” (L2) | 1247,94                  | 113,14            | 21,85           | 42,39            | 26,78          | 7,1               | Sawtooth                      |

<img src="media\image119.png" style="width:6.26806in;height:4.16482in" />

G 106: Frequency and power measurement of jammer H6.2 on antenna “4”
(L1)

<img src="media\image120.png" style="width:6.27083in;height:4.16667in" />

G 107: Frequency and power measurement with wider band of jammer H6.2 on
antenna “4” (L1)

<img src="media\image121.png" style="width:6.27083in;height:4.16667in" />

G 108: Frequency and power measurement of jammer H6.2 on antenna “5”
(L5)

<img src="media\image122.png" style="width:6.27083in;height:4.16667in" />

G 109: Frequency and power measurement of jammer H6.2 on antenna “6”
(L2)

<img src="media\image123.png" style="width:6.27083in;height:4.16667in" />

G 110: Real-time persistence and spectrogram measurement of jammer H6.2
on antenna “4” (L1)

<img src="media\image124.png" style="width:6.27083in;height:4.16667in" />

G 111: Real-time persistence and spectrogram measurement with wider span
of jammer H6.2 on antenna “4” (L1)

<img src="media\image125.png" style="width:6.27083in;height:4.16667in" />

G 112: Real-time persistence and spectrogram measurement of jammer H6.2
on antenna “5” (L5)

<img src="media\image126.png" style="width:6.27083in;height:4.16667in" />

G 113: Real-time persistence and spectrogram measurement of jammer H6.2
on antenna “6” (L2)

<img src="media\image127.png" style="width:6.27083in;height:4.16667in" />

G 114: Time domain (analog demod) measurement with wider sweep of jammer
H6.2 on antenna “4” (L1)

<img src="media\image128.png" style="width:6.27083in;height:4.16667in" />

G 115: Time domain (analog demod) measurement of jammer H6.2 on antenna
“5” (L5)

<img src="media\image129.png" style="width:6.27083in;height:4.16667in" />

G 116: Time domain (analog demod) measurement of jammer H6.2 on antenna
“6” (L2)

### Technical details on low-power jammer “H6.3”

<img src="media\image118.jpeg" style="width:1.98056in;height:2.1375in" />
The jammer H6.3 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H6.3 is a six-antenna, so-called “multi-frequency”, jammer. It jams six
different bands, but only three channels are relevant for GNSS bands
(“L1+L2+L5”), thus disrupting the upper and lower L-band.

The relevant antennas are marked with numbers: “4” (L1), “5” (L5) and
“6” (L2).

<u>Technical characteristics of H6.3 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “4” (L1) | 1581,37                  | 26,50             | 25,54           | 39,77            | 25,46          | 7,1               | Sawtooth   |
| “5” (L5) | 1152,73                  | 112,05            | 19,50           | 39,99            | 24,36          | 7,06              | Sawtooth   |
| “6” (L2) | 1248,65                  | 111,06            | 21,80           | 42,25            | 26,65          | 7,08              | Sawtooth   |

<img src="media\image130.png" style="width:6.27083in;height:4.16667in" />

G 117: Frequency and power measurement of jammer H6.3 on antenna “4”
(L1)

<img src="media\image131.png" style="width:6.27083in;height:4.16667in" />

G 118: Frequency and power measurement of jammer H6.3 on antenna “5”
(L5)

<img src="media\image132.png" style="width:6.27083in;height:4.16667in" />

G 119: Frequency and power measurement of jammer H6.3 on antenna “6”
(L2)

<img src="media\image133.png" style="width:6.27083in;height:4.16667in" />

G 120: Real-time persistence and spectrogram measurement of jammer H6.3
on antenna “4” (L1)

<img src="media\image134.png" style="width:6.27083in;height:4.16667in" />

G 121: Real-time persistence and spectrogram measurement with wider span
of jammer H6.3 on antenna “4” (L1)

<img src="media\image135.png" style="width:6.27083in;height:4.16667in" />

G 122: Real-time persistence and spectrogram measurement of jammer H6.3
on antenna “5” (L5)

<img src="media\image136.png" style="width:6.27083in;height:4.16667in" />

G 123: Real-time persistence and spectrogram measurement of jammer H6.3
on antenna “6” (L2)

<img src="media\image137.png" style="width:6.27083in;height:4.16667in" />

G 124: Time domain (analog demod) measurement of jammer H6.3 on antenna
“4” (L1)

<img src="media\image138.png" style="width:6.27083in;height:4.16667in" />

G 125: Time domain (analog demod) measurement with wider sweep of jammer
H6.3 on antenna “4” (L1)

<img src="media\image139.png" style="width:6.27083in;height:4.16667in" />

G 126: Time domain (analog demod) measurement of jammer H6.3 on antenna
“5” (L5)

<img src="media\image140.png" style="width:6.27083in;height:4.16667in" />

G 127: Time domain (analog demod) measurement of jammer H6.3 on antenna
“6” (L2)

### Technical details on low-power jammer “H6.4”
<img src="media\image141.png" style="width:2.125in;height:2.83194in" />

The jammer H6.4 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H6.4 is a six-antenna, so-called “multi-frequency”, jammer. It jams six
different bands, but only three channels are relevant for GNSS bands
(“L1+L2+L5”), thus disrupting the upper and lower L-band.

The relevant antennas are marked with numbers: “1” (L5), “3” (L2) and
“5” (L1)

<u>Technical characteristics of H6.4 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “1” (L5) | 1176,66                  | 17,23             | 16,54           | 28,91            | 19,30          | 10,62             | Triangle   |
| “3” (L2) | 1248,01                  | 85,41             | 23,54           | 42,86            | 26,15          | 10,3              | Triangle   |
| “5” (L1) | 1593,36                  | 81,28             | 22,82           | 41,92            | 25,63          | 11                | Triangle   |

<img src="media\image142.png" style="width:6.27083in;height:4.16667in" />

G 128: Frequency and power measurement of jammer H6.4 on antenna “1”
(L5)

<img src="media\image143.png" style="width:6.26806in;height:4.4043in" />

G 129: Frequency and power measurement of jammer H6.4 on antenna “3”
(L2)

<img src="media\image144.png" style="width:6.27083in;height:4.40625in" />

G 130: Frequency and power measurement of jammer H6.4 on antenna “5”
(L1)

<img src="media\image145.png" style="width:6.27083in;height:4.16667in" />

G 131: Real-time persistence and spectrogram measurement of jammer H6.4
on antenna “1” (L5)

<img src="media\image146.png" style="width:6.27083in;height:4.40625in" />

G 132: Real-time persistence and spectrogram measurement of jammer H6.4
on antenna “3” (L2)

<img src="media\image147.png" style="width:6.27083in;height:4.40625in" />

G 133: Real-time persistence and spectrogram measurement of jammer H6.4
on antenna “5” (L1)

<img src="media\image148.png" style="width:6.27083in;height:4.16667in" />

G 134: Time domain (analog demod) measurement of jammer H6.4 on antenna
“1” (L5)

<img src="media\image149.png" style="width:6.27083in;height:4.40625in" />

G 135: Time domain (analog demod) measurement of jammer H6.4 on antenna
“3” (L2)

<img src="media\image150.png" style="width:6.27083in;height:4.40625in" />

G 136: Time domain (analog demod) measurement of jammer H6.4 on antenna
“5” (L1)

### Technical details on low-power jammer “H6.5”
<img src="media\image141.png" style="width:2.125in;height:2.83194in" />

The jammer H6.5 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H6.5 is a six-antenna, so-called “multi-frequency”, jammer. It jams six
different bands, but only three channels are relevant for GNSS bands
(“L1+L2+L5”), thus disrupting the upper and lower L-band.

The relevant antennas are marked with numbers: “1” (L5), “3” (L2) and
“5” (L1)

<u>Technical characteristics of H6.5 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “1” (L5) | 1180,33                  | 24,28             | 24,73           | 38,58            | 27,66          | 10,26             | Triangle   |
| “3” (L2) | 1247,05                  | 82,22             | 23,22           | 42,37            | 25,77          | 10,32             | Triangle   |
| “5” (L1) | 1595,6                   | 80,12             | 22,62           | 41,65            | 25,41          | 10,3              | Triangle   |

<img src="media\image151.png" style="width:6.27083in;height:4.40625in" />

G 137: Frequency and power measurement of jammer H6.5 on antenna “1”
(L5)

<img src="media\image152.png" style="width:6.27083in;height:4.40625in" />

G 138: Frequency and power measurement of jammer H6.5 on antenna “3”
(L2)

<img src="media\image153.png" style="width:6.27083in;height:4.40625in" />

G 139: Frequency and power measurement of jammer H6.5 on antenna “5”
(L1)

<img src="media\image154.png" style="width:6.27083in;height:4.40625in" />

G 140: Real-time persistence and spectrogram measurement of jammer H6.5
on antenna “1” (L5)

<img src="media\image155.png" style="width:6.27083in;height:4.40625in" />

G 141: Real-time persistence and spectrogram measurement of jammer H6.5
on antenna “3” (L2)

<img src="media\image156.png" style="width:6.27083in;height:4.40625in" />

G 142: Real-time persistence and spectrogram measurement of jammer H6.5
on antenna “5” (L1)

<img src="media\image157.png" style="width:6.27083in;height:4.40625in" />

G 143: Time domain (analog demod) measurement of jammer H6.5 on antenna
“1” (L5)

<img src="media\image158.png" style="width:6.27083in;height:4.40625in" />

G 144: Time domain (analog demod) measurement of jammer H6.5 on antenna
“3” (L2)

<img src="media\image159.png" style="width:6.27083in;height:4.40625in" />

G 145: Time domain (analog demod) measurement of jammer H6.5 on antenna
“5” (L1)

### Technical details on low-power jammer “H6.6”
<img src="media\image141.png" style="width:2.125in;height:2.83194in" />

The jammer H6.6 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H6.6 is a six-antenna, so-called “multi-frequency”, jammer. It jams six
different bands, but only three channels are relevant for GNSS bands
(“L1+L2+L5”), thus disrupting the upper and lower L-band.

The relevant antennas are marked with numbers: “1” (L5), “3” (L2) and
“5” (L1)

<u>Technical characteristics of H6.6 (2024 measurements)</u>

| Antenna  | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “1” (L5) | 1178,53                  | 21,01             | 24,93           | 38,15            | 27,94          | 10,00             | Triangle   |
| “3” (L2) | 1247,30                  | 88,06             | 23,65           | 43,10            | 26,28          | 9,92              | Triangle   |
| “5” (L1) | 1592,48                  | 73,60             | 22,84           | 41,51            | 25,60          | 10,46             | Triangle   |

<img src="media\image160.png" style="width:6.27083in;height:4.40625in" />

G 146: Frequency and power measurement of jammer H6.6 on antenna “1”
(L5)

<img src="media\image161.png" style="width:6.27083in;height:4.40625in" />

G 147: Frequency and power measurement of jammer H6.6 on antenna “3”
(L2)

<img src="media\image162.png" style="width:6.27083in;height:4.40625in" />

G 148: Frequency and power measurement of jammer H6.6 on antenna “5”
(L1)

<img src="media\image163.png" style="width:6.27083in;height:4.40625in" />

G 149: Real-time persistence and spectrogram measurement of jammer H6.6
on antenna “1” (L5)

<img src="media\image164.png" style="width:6.27083in;height:4.40625in" />

G 150: Real-time persistence and spectrogram measurement of jammer H6.6
on antenna “3” (L2)

<img src="media\image165.png" style="width:6.27083in;height:4.40625in" />

G 151: Real-time persistence and spectrogram measurement of jammer H6.6
on antenna “5” (L1)

<img src="media\image166.png" style="width:6.27083in;height:4.40625in" />

G 152: Time domain (analog demod) measurement of jammer H6.6 on antenna
“1” (L5)

<img src="media\image167.png" style="width:6.27083in;height:4.40625in" />

G 153: Time domain (analog demod) measurement of jammer H6.6 on antenna
“3” (L2)

<img src="media\image168.png" style="width:6.27083in;height:4.40625in" />

G 154: Time domain (analog demod) measurement of jammer H6.6 on antenna
“5” (L1)

### Technical details on low-power jammer “F6.1”
<img src="media\image169.png" style="width:2.19583in;height:2.92639in" />

The jammer F6.1 belongs to the ‘Permanently installed (Fixed)’ of
jammers. It is a large and heavy tabletop type of jammer, in need of
constant power supply with a relatively easy operation, just an
on/off-button with a LED-light to indicate activation and DIP switches
to change between channels.

F6.1 is a six-antenna, so-called “multi-frequency”, jammer. It jams six
different bands, but only four channels are relevant for GNSS bands
(“L1+L2+L5”), thus disrupting the upper and lower L-band.

The relevant antennas are marked with letters and numbers: “F2” (L1),
“F3” (L1), “F4” (L2) and “F6” (L5)

This jammer has the possibility to adjust the output power, with a power
control knob for each antenna. The measurements below are all done at
maximum power.

<u>Technical characteristics of F6.1 (2024 measurements)</u>

| Antenna   | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation          |
|-----------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|---------------------|
| “F2” (L1) | 1592,59                  | 66,55             | 31,49           | 49,72            | 34,85          | 6,46 / 98,50      | sinus / FM-modulert |
| “F3” (L1) | 1589,40                  | 73,75             | 27,45           | 46,13            | 29,14          | 6,24              | sinus               |
| “F4” (L2) | 1243,65                  | 76,22             | 25,42           | 44,24            | 26,94          | 6,20 / 155,00     | sinus / FM-modulert |
| “F6” (L5) | 1177,93                  | 16,58             | 24,93           | 37,13            | 18,51          | 5,96              | sinus               |

<img src="media\image170.png" style="width:6.27083in;height:4.40625in" />

G 155: Frequency and power measurement of jammer F6.1 on antenna “F2”
(L1)

<img src="media\image171.png" style="width:6.27083in;height:4.40625in" />

G 156: Frequency and power measurement of jammer F6.1 on antenna “F3”
(L1)

<img src="media\image172.png" style="width:6.27083in;height:4.40625in" />

G 157: Frequency and power measurement of jammer F6.1 on antenna “F4”
(L2)

<img src="media\image173.png" style="width:6.27083in;height:4.40625in" />

G 158: Frequency and power measurement of jammer F6.1 on antenna “F6”
(L5)

<img src="media\image174.png" style="width:6.27083in;height:4.40625in" />

G 159: Real-time persistence and spectrogram measurement of jammer F6.1
on antenna “F2” (L1)

<img src="media\image175.png" style="width:6.27083in;height:4.40625in" />

G 160: Real-time persistence and spectrogram measurement of jammer F6.1
on antenna “F3” (L1)

<img src="media\image176.png" style="width:6.27083in;height:4.40625in" />

G 161: Real-time persistence and spectrogram measurement of jammer F6.1
on antenna “F4” (L2)

<img src="media\image177.png" style="width:6.27083in;height:4.40625in" />

G 162: Real-time persistence and spectrogram measurement of jammer F6.1
on antenna “F6” (L5)

<img src="media\image178.png" style="width:6.27083in;height:4.40625in" />

G 163: Time domain (analog demod) measurement of jammer F6.1 on antenna
“F2” (L1)

<img src="media\image179.png" style="width:6.27083in;height:4.26042in" />

G 164: Time domain (analog demod) measurement with wider span of jammer
F6.1 on antenna “F2” (L1)

<img src="media\image180.png" style="width:6.27083in;height:4.40625in" />

G 165: Time domain (analog demod) measurement of jammer F6.1 on antenna
“F3” (L1)

<img src="media\image181.png" style="width:6.27083in;height:4.11458in" />

G 166: Time domain (analog demod) measurement with wider span of jammer
F6.1 on antenna “F3” (L1)

<img src="media\image182.png" style="width:6.27083in;height:4.40625in" />

G 167: Time domain (analog demod) measurement of jammer F6.1 on antenna
“F4” (L2)

<img src="media\image183.png" style="width:6.27083in;height:4.0625in" />

G 168: Time domain (analog demod) measurement with wider span of jammer
F6.1 on antenna “F4” (L2)

<img src="media\image184.png" style="width:6.27083in;height:4.40625in" />

G 169: Time domain (analog demod) measurement of jammer F6.1 on antenna
“F6” (L5)

<img src="media\image185.png" style="width:6.27083in;height:4.19792in" />

G 170: Time domain (analog demod) measurement with wider span of jammer
F6.1 on antenna “F6” (L5)

### Technical details on low-power jammer H8.1
<img src="media\image186.png" style="width:1.68611in;height:2.57917in" />

The jammer H8.1 belongs to the ‘Handheld category’ of jammers. It is a
larger but relatively light battery driven jammer with a relatively easy
operation, just an on/off-button with a LED-light to indicate activation
and DIP switches to change between channels.

H8.1 is a eight-antenna, so-called “multi-frequency”, jammer, but not a
“multi-GNSS-jammer”. It jams eight different bands, but only one
GNSS-band (“L1-only”), so disrupting only the upper L-band.

Relevant GNSS antenna is marked: “6”

<u>Technical characteristics of H8.1 (2024 measurements)</u>

| Antenna | Centre frequency \[MHz\] | Bandwidth \[MHz\] | PSD \[dBm/MHz\] | TX total \[dBm\] | CF max \[dBm\] | Sweep rate \[µs\] | Modulation |
|---------|--------------------------|-------------------|-----------------|------------------|----------------|-------------------|------------|
| “6”     | 1593,30                  | 77,14             | 23,48           | 42,35            | 26,59          | 10,47             | Triangle   |

<img src="media\image187.png" style="width:6.27083in;height:4.16667in" />

G 171: Frequency and power measurement of jammer H8.1 on antenna “6”

<img src="media\image188.png" style="width:6.27083in;height:4.16667in" />

G 172: Real-time persistence and spectrogram measurement of jammer H8.1
on antenna “6”

<img src="media\image189.png" style="width:6.27083in;height:4.16667in" />

G 173: Time domain (analog demod) measurement of jammer H8.1 on antenna
“6”

### Technical details on the meaconing setup “Porcellum” / “F1.1”

The meaconing setup consists of two GNSS antennas “E1” and “E2” at two
respective locations some distance from the transmitting antenna. Real
live sky signals from the receivers are (after travelling through long
cables) retransmitted with a directional antenna “E3” pointing towards
the community house in Bleik. The locations of the receiving antennas
are outside of the line-of-sight to the transmitter antenna to avoid a
feedback loop. The setup allows for switching between the two receiving
antennas, ramping power and simultaneous transmission of both signals.

<img src="media\image190.png" style="width:6.74687in;height:3.32292in" />

G 174: Diagram of the meaconing setup

### Technical details on the high-power jammer “Porcus Maior”/ “F8.1”

The high-power jammer provides jamming signals with up to 50 W EIRP
simultaneously on eight GNSS bands, where the maximum available power
depends on the signal modulations. Figure G 176 is a block diagram of
the high-power jammer that shows how it works in pniciple. The jammer
uses two USRP X410 SDR from Ettus Research as exciters. Each SDR have
four output channels covering the frequency range of 1 MHz to 7.2 GHz,
with maximum 400 MHz instantaneous bandwidth. The SDRs have an internal
gain range of 60 dB in 1 dB steps. Each of the exciter output signals
are fed to the corresponding channel of the programmable
step-attenuator. The jammer can also utilize other signal generators.
The attenuator has an attenuation range of 95 dB in 0.25 dB steps. The
output signal from the attenuators is then fed to the power amplifiers.
The amplifiers connect to eight individual antennas via around 10 m coax. The
antennas are directional helical antennas with right hand circular
polarization (RHCP) and 10 dB gain.

An overview of the jammer signal modulations is given in G 175.

| **Frequency band name** | **CW**              | **PRN**                    | **Frequency sweep**     |                            |                       |                               |
|-------------------------|---------------------|----------------------------|-------------------------|----------------------------|-----------------------|-------------------------------|
|                         | **Frequency (MHz)** | **Center frequency (MHz)** | **BPSK chiprate (MHz)** | **Center frequency (MHz)** | **Sweep rates (kHz)** | **Frequency bandwidth (MHz)** |
| **L1**                  | 1575.42             | 1575.42                    | 10                       | 1575.42                    | 1-100                 | 20                             |
| **L2**                  | 1227.6              | 1227.6                     | 10                       | 1227.6                     | 1-100                 | 20                             |
| **L5**                  | 1176.45             | 1176.45                    | 10                       | 1176.45                    | 1-100                 | 20                             |
| **G1**                  | 1602                | 1602                       | 5                        | 1602                       | 1-100                 | 10                             |
| **G2**                  | 1246                | 1246                       | 10                       | 1246                       | 1-100                 | 20                             |
| **E5b**                 | 1207.14             | 1207.14                    | 10                       | 1207.14                    | 1-100                 | 20                             |
| **E6**                  | 1278.75             | 1278.75                    | 10                       | 1278.75                    | 1-100                 | 20                             |
| **B1I**                 | 1561.098            | 1561.098                   | 1                        | 1561.098                   | 1-100                 | 2                              |

G 175: Overview of the signal modulations employed by ‘Porcus Major’

A PC controls the high-power jammer, that is both exciters and the
step-attenuators. Software allows for the jammer to automatically
execute individual tests described for the high-power jammer and
supports all jamming signals described therein.

The high-power jammer is connected to Internet and time synchronized
using Network Time Protocol (NTP). After a jamming activity, it can
upload the activity log to the central server.

<img src="media\image191.jpg" style="width:6.76795in;height:5.10417in" alt="Et bilde som inneholder tekst, diagram, skjermbilde, line Automatisk generert beskrivelse" />

G 176: Diagram of the high-power jammer

### Technical details on software defined radio mobile SDR spoofer “F1.2”

A software defined radio (SDR) of type BladeRF x115 from Nuand is used
for the mobile spoofing tests. The output signal is amplified 45 dB
through an AA MCS 800 – 2200MHz amplifier, so that the maximum total
EIRP is about 10 dBm. This signal is transmitted by a dipole antenna on
the top of the vehicle, see [ds1036-080410.pdf
(european-antennas.co.uk).](https://www.european-antennas.co.uk/media/1900/ds1036-080410.pdf)

<img src="media\image192.png" style="width:3.53125in;height:3.53125in" />

G 177: Picture of the SDR without casing

The spoofed signals are GPS C/A only and may be combined with Glonass
jamming (G1).
