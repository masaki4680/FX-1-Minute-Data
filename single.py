from histdata import download_hist_data as dl
from histdata.api import Platform as P, TimeFrame as TF

dl(year='2021', month='4', pair='eurusd',
   platform=P.GENERIC_ASCII, time_frame=TF.ONE_MINUTE)
