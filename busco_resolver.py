import re

class busco_resolver:
    def __init__(self, busco_summary):
        self.busco_summary = busco_summary
        self.busco_summary_str = ''

        with open(busco_summary) as bf:
            for line in bf:
                self.busco_summary_str += line
            busco_summary_re = re.compile(r'C:(.+)%\[S:(.+)%,D:(.+)%\],F:(.+)%,M:(.+)%,n:(\d+).+\n\t(\d+)\tComplete BUSCOs \(C\)\t\t\t   \n\t(\d+)\tComplete and single-copy BUSCOs \(S\)\t   \n\t(\d+)\tComplete and duplicated BUSCOs \(D\)\t   \n\t(\d+)\tFragmented BUSCOs \(F\)\t\t\t   \n\t(\d+)\tMissing BUSCOs \(M\)\t\t\t   \n\t(\d+)\tTotal BUSCO groups searched')
            self.res_lis = busco_summary_re.findall(self.busco_summary_str)
    
        self.busco_count = (float(self.res_lis[6]) + float(self.res_lis[9])) / float(self.res_lis[11])
