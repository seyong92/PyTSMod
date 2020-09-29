TSMOD_DESC = 'Processing time-scale modification for given audio file.'
SUBPARSER_HELP = 'Available TSM algorithms'

INPUT_HELP = 'Input audio file to modify.'
OUTPUT_HELP = 'Output file path to save.'

A_HELP = 'The time stretching factor alpha.'
WT_HELP = 'Type of the window function. hann and sin are available.'
WS_HELP = 'Size of the window function.'
SH_HELP = 'Hop size of the synthesis window.'

OLA_HELP = 'Using OLA to modify audio file.'
OLA_DESC = 'Using OLA to modify audio file.'

WSOLA_HELP = 'Using WSOLA to modify audio file.'
WSOLA_DESC = 'Using WSOLA to modify audio file.'
TOL_HELP = 'Number of samples the window positions in the input signal may be shifted'

PV_HELP = 'Using phase vocoder to modify audio file.'
PV_DESC = 'Using phase vocoder to modify audio file.'
ZP_HELP = 'The size of the zero pad in the window function.'
RE_HELP = 'Try to reserve potential energy loss.'
FS_HELP = 'Apply circular shift to STFT and ISTFT.'
PL_HELP = 'Apply phase locking.'

PVI_HELP = 'Using phase vocoder specialized for integer stretching factor.'
PVI_DESC = 'Using phase vocoder specialized for integer stretching factor.'
A_PVI_HELP = 'The time stretching factor alpha. Only integer value is allowed.'
