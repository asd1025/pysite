class Paging:
    groupCount = 5
    contentsCount=10

    def __init__(self,allCount=0,allPageCount=0):
        self.allCount = allCount
        self.prevGroupNo=0
        self.startPageNo=0
        self.startPageGroupNo=0
        self.allPageCount = int(allCount/Paging.contentsCount) if ((allCount % Paging.contentsCount) == 0) else (int(allCount/Paging.contentsCount) + 1)
        self.allGroupCount = int(allPageCount/Paging.groupCount) if ((allPageCount % Paging.groupCount) == 0) else (int(allPageCount/Paging.groupCount) + 1)
        self.setPageNo(self)


    def getStartPageGroupNo(self):
        return Paging.groupCount * int(self.prevGroupNo)

    def getStartPageNo(self):
        self.pageNo = 1 if int(self.pageNo) < 1 else self.pageNo
        return (int(self.pageNo)-1) * Paging.contentsCount

    def setPageNo(self,pageNo=1):
        if pageNo == 1:
            self.pageNo = int(self.prevGroupNo) * int(self.groupCount) + 1
        else :
            self.pageNo= pageNo
    def getAllPageCount(self):
        return int(self.allCount / Paging.contentsCount) if (self.allCount % Paging.contentsCount) == 0 else int(self.allCount / Paging.contentsCount) + 1

    def getAllGroupCount(self):
        return int(self.allPageCount / Paging.groupCount) if (self.allPageCount % Paging.groupCount) == 0 else int(self.allPageCount / Paging.groupCount) + 1

    def getPaging(self,prevGroupNo=0,pageNo=1):
        self.prevGroupNo=prevGroupNo
        self.setPageNo(pageNo)
        self.allPageCount=self.getAllPageCount()
        self.allGroupCount=self.getAllGroupCount()
        self.startPageGroupNo=self.getStartPageGroupNo()
        self.startPageNo=self.getStartPageNo()
        return self

    def __str__(self):
        return f'Paging [allCount={self.allCount}, groupCount={self.groupCount}, prevGroupNo={self.prevGroupNo}, contentsCount={self.contentsCount}, allPageCount= {self.allPageCount} , allGroupCount= {self.allGroupCount}, pageNo={self.pageNo}, startPageNo={self.startPageNo}, startPageGroupNo={self.startPageGroupNo}'



