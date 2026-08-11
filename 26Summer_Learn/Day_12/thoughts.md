好了

我承认withopen不如Path好用

withopen又要缩进又不能直接写入json

withopen似乎更适合写入txt格式文本

要是想要改变json的话

可以通过path.loads(),先转出json

再通过dic的增减变化，然后再转回json

或者直接通过write_text来直接覆盖

都会比withopen好用得多