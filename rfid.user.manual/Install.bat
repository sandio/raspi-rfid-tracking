copy rfidx.ocx %systemroot%\system32 /y
copy mscomm32.ocx %systemroot%\system32 /y
regsvr32 /u %systemroot%\system32\rfidx.ocx
regsvr32 %systemroot%\system32\rfidx.ocx
regsvr32 /u %systemroot%\system32\mscomm32.ocx
regsvr32 %systemroot%\system32\mscomm32.ocx
