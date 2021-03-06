from datetime import datetime
from readgssi.__init__ import __version__, name
import pkg_resources


dist = pkg_resources.get_distribution(name)
year = datetime.now().year
author = 'Ian Nesbitt'
affil = 'School of Earth and Climate Sciences, University of Maine'

help_text = u'''Help text:
############################################################
 readgssi version %s

 Copyleft %s %s 2017-%s
 %s
############################################################

usage:
readgssi -i input.DZT [OPTIONS]

optional flags:
     OPTION     |      ARGUMENT       |       FUNCTIONALITY
-o, --output    | file:  /dir/f.ext   |  specify an output file
-f, --format    | string, eg. "csv"   |  specify output format (csv is the only working format currently)
-p, --plot      | +integer or "auto"  |  plot will be x inches high (dpi=150), or "auto". default: 10
-n, --noshow    |                     |  suppress matplotlib popup window and simply save a figure (useful for multiple file processing)
-c, --colormap  | string, eg. "Greys" |  specify the colormap (https://matplotlib.org/users/colormaps.html#grayscale-conversion)
-g, --gain      | positive (+)integer |  gain value (higher=greater contrast, default: 1)
-r, --bgr       |                     |  horizontal background removal algorithm (useful to remove ringing)
-R, --reverse   |                     |  reverse (flip radargram horizontally)
-w, --dewow     |                     |  trinomial dewow algorithm
-t, --bandpass  | +int-+int (MHz)     |  butterworth bandpass filter (positive integer range in megahertz; ex. 100-145)
-b, --colorbar  |                     |  add a colorbar to the radar figure
-a, --antfreq   | positive integer    |  specify antenna frequency (read automatically if not given)
-s, --stack     | +integer or "auto"  |  specify trace stacking value or "auto" to autostack to ~2.5:1 x:y axis ratio
-N, --normalize | "auto" or .csv file |  if "auto", use DZG GPS file; otherwise must point at a csv file with lat, lon, and time fields to distance normalize with
-m, --histogram |                     |  produce a histogram of data values
-z, --zero      | positive integer    |  skip this many samples from the top of the trace downward (useful for removing transceiver delay)
''' % (__version__, u'\U0001F12F', author, year, affil)
