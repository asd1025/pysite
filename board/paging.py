class Paging:
    #allCount=0
    groupCount = 5
    #prevGroupNo=0
    contentsCount=10
    #allPageCount=0
    #allGroupCount=0
    #pageNo = 1
    #startPageNo=0
    #startPageGroupNo=0

    def __init__(self,allCount,allPageCount=0):
        self.allCount = allCount
        self.pageNo = 1
        self.prevGroupNo=0
        self.startPageNo=0
        self.startPageGroupNo=0
        self.allPageCount = int(allCount/Paging.contentsCount) if ((allCount%Paging.contentsCount) == 0) else (int(allCount/Paging.contentsCount) + 1)
        self.allGroupCount = int(allPageCount/Paging.groupCount) if ((allPageCount % Paging.groupCount) == 0) else (int(allPageCount/Paging.groupCount) + 1)


    def getStartPageGroupNo(self):
        return Paging.groupCount * self.prevGroupNo

    def getStartPageNo(self):
        self.pageNo = 1 if self.pageNo < 1 else self.pageNo
        return (self.pageNo-1) * Paging.contentsCount

    def setPageNo(self,pageNo):
        if pageNo == 1:
            self.pageNo = self.prevGroupNo * self.groupCount + 1
    def getAllPageCount(self):
        return int(self.allCount / Paging.contentsCount) if (self.allCount % Paging.contentsCount) == 0 else int(self.allCount / Paging.contentsCount) + 1

    def getAllGroupCount(self):
        return int(Paging.allPageCount / Paging.groupCount) if (Paging.allPageCount % Paging.groupCount) == 0 else int(Paging.allPageCount / Paging.groupCount) + 1

    def __str__(self):
        return f'Paging [allCount={self.allCount}, groupCount={self.groupCount}, prevGroupNo={self.prevGroupNo} \
			    contentsCount={self.contentsCount}, allPageCount= {self.allPageCount} , allGroupCount= {self.allGroupCount} \
			    pageNo={self.pageNo}, startPageNo={self.startPageNo}, startPageGroupNo={self.startPageGroupNo}'



