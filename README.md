FMT
======

This project is for receiving the ARRL Frequency Measurement Test with the USRP, GNU Radio, and Baudline.  A video detailing the project may be found here:

http://youtu.be/_brT8AElZi0

Author: Louis Brown KD4HSO

Tested with:
- Ettus X310 + LFRX + GPSDO (http://www.ettus.com)
- Ettus UHD 3.8.0 (https://github.com/EttusResearch/uhd)
- GNU Radio 3.7.6 (https://github.com/gnuradio/gnuradio)
- Baudline 1.09 beta6n (http://www.baudline.com)
- ARRL FMT (http://www.arrl.org/frequency-measuring-test)

I measured sub-Hz accuracy in the November, 2014 test, although I feel I could have done better on the 80m and 160m signals since they had stronger SNR.  The 40m signal was a mess.

http://www.b4h.net/fmt/fmtresults201411.php
![Nov 14 result](https://github.com/madengr/fmt/blob/master/fmt_Nov14_kd4hso.png)


See the video for a detailed overview.  The USRP X310 directly (real) samples the RF at 200 Msps from an active loop antenna via the LFRX daughter-card.  The USRP tunes with it's DDC and decimates to 250 ksps quadrature stream into GNU Radio flow graph.  GNU Radio fine tunes, decimates to 2500 sps, and records to disk.  The USRP DDC frequency is calculated to uHz precision for file name stamping.  Realtime audio is offset by a 600 Hz BFO, filtered to 100 Hz BW, and leveled with an AGC.  Channel power is calculated and sampled with a probe.  
    
![GRC flow screenshot](https://github.com/madengr/fmt/blob/master/fmt_grc.png)

![GUI screenshot](https://github.com/madengr/fmt/blob/master/fmt_gui.png)

Baudline performs a large FFT and the frequency estimation tool is used to find the offset from the LO.

![Baudline screenshot](https://github.com/madengr/fmt/blob/master/fmt_baudline.png)
