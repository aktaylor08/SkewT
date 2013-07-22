======================================================
SkewT -- Atmospheric Profile Plotting and Diagnostics
======================================================

SkewT provides a few useful tools to help with the plotting and analysis of 
upper atmosphere data. In particular it provides some useful classes to 
handle the awkward skew-x projection (provided by Ryan May, see notes in 
source code and LICENSE.txt).

It's most basic implementation is to read a text file of the format provided 
by the University of Wyoming's website: 

http://weather.uwyo.edu/upperair/sounding.html

Typical usage often looks like this::

    #!/usr/bin/env python

    from skewt import SkewT
    sounding = SkewT.Sounding(filename="soundingdata.txt")
    sounding.plot_skewt()

Alternatively you may input the required data fields in a dictionary. The 
dictionary must have as a minimum the fields PRES and TEMP corresponding to 
pressure (hPa) and temperature (deg C). Soundings will typically have a dew 
point temperature trace and wind barbs as well, so it's best to include the 
dewpoint temp DWPT (deg C), wind speed SKNT (knots) and wind direction in 
degrees WDIR. Other fields may be included as per the docstring::

    #!/usr/bin/env python

    from skewt import SkewT
    sounding = SkewT.Sounding(data=data_dict)
    sounding.plot_skewt

News
====
I was so thrilled to see that there were something like 80 downloads in the 
first week that I dropped everything else and pushed through some changes I 
had been meaning to make. Thanks for your interest in this package and I'd 
love to hear your feedback: thomas.chubb AT monash.edu

Here's a summary of what's new in this release:

* Added a parcel ascent routine based on provided pressure, dewpoint and 
  temperature. This routine adds some characteristics to the plot in the 
  upper LHS. TODO: initialise parcels automatically, calculate CAPE and CIN 
  and Precipitable water... 
* Removed reliance on rcParams to make the figure look pretty. Did this 
  because I got annoyed (and I'm sure that others will too) at what happens 
  to graphs plotted subsequently... they end up with yellow axes etc.
* Improved some of the aesthetics of the plot... moved standard atmosphere 
  height axis to right hand side.

Sounding Files
==============
The format for the sounding files is very specific (sorry). You are best off 
using the example in "examples" as a template. Here's a sample of the first 
few lines::

    94975 YMHB Hobart Airport Observations at 00Z 02 Jul 2013

    -----------------------------------------------------------------------------
       PRES   HGHT   TEMP   DWPT   RELH   MIXR   DRCT   SKNT   THTA   THTE   THTV
	hPa     m      C      C      %    g/kg    deg   knot     K      K      K 
    -----------------------------------------------------------------------------
     1004.0     27   12.0   10.2     89   7.84    330     14  284.8  306.7  286.2
     1000.0     56   12.4   10.3     87   7.92    325     16  285.6  307.8  286.9
      993.0    115   12.8    9.7     81   7.66    311     22  286.5  308.1  287.9

The script defines columns by character number so you really do have to get 
the format *exactly* right. One day I will get around to writing a routine 
to output the text files properly.

Parcel Ascent (New in version 0.1.2!)
=====================================
Simple routine to calculate the characteristics of a parcel initialised with 
pressure, temperature and dew point temperature. You could do it like this::

    from skewt import SkewT

    sounding=SkewT.Sounding("examples/94975.2013070200.txt")
    sounding.make_skewt_axes()
    sounding.add_profile(color='r',lw=2)
    sounding.lift_parcel(1004.,17.4,8.6)
    draw()
 
The parcel properties are manually input at this point. For the example 
above (BOM), I believe that the temperature was the forecast maximum for the 
day and the dewpoint temp was derived by taking the average mixing ratio 
from the lowest 50 (100??) mb and calculating the corresponding dew point 
temperature for the surface pressure at the sounding time.

To-Do List
==========
* I want to do some basic diagnostics given the lifted parcel. This 
  shouldn't be hard it's just that I have more pressing things to do. If 
  anybody out there wants to adapt/contribute routines that they have I'd be 
  most grateful. Send your fan/hate mail to thomas.chubb AT monash.edu

* Hodographs?

Contributors
==============

  * Simon Caine is the latest recruit (yay)

  * Hamish Ramsay has promised to at least think about adding some extra 
  diagnostics.

  * The initial SkewX classes were provided by a fellow called Ryan May who 
  was a student at OU. I have not made contact with Ryan other than to 
  download his scripts and modify them for my own purposes.

