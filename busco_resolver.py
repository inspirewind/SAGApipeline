import re

class busco_resolver:
    def __init__(self, busco_summary):
        def get_busco_summary(self) -> list:
            busco_summary_str = ''
            with open(self.busco_summary) as bf:
                for line in bf:
                    busco_summary_str += line
            busco_summary_re = re.compile(r'C:(.+)%\[S:(.+)%,D:(.+)%\],F:(.+)%,M:(.+)%,n:(\d+).+\n\t(\d+)\tComplete BUSCOs \(C\)\t\t\t   \n\t(\d+)\tComplete and single-copy BUSCOs \(S\)\t   \n\t(\d+)\tComplete and duplicated BUSCOs \(D\)\t   \n\t(\d+)\tFragmented BUSCOs \(F\)\t\t\t   \n\t(620)\tMissing BUSCOs \(M\)\t\t\t   \n\t(\d+)\tTotal BUSCO groups searched\t\t   \n')
            res_lis = busco_summary_re.findall(busco_summary_str)
            return res_lis[0]

        def get_busco_count(self) -> float:
            # make sure the busco_summary is parsed in fixed format
            return (float(self.res_lis[6]) + float(self.res_lis[9])) / float(self.res_lis[11])
            
        self.busco_summary = busco_summary
        self.res_lis = get_busco_summary(self.busco_summary)
        self.busco_count = get_busco_count(self.res_lis)

        


    