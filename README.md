# tcharai
A TUI script for interacting with CharacterAI using Python
![](https://github.com/niizam/tcharai/blob/main/tcharai.gif)
Install requirements
```
pip install playwright
playwright install firefox
pip install windows-curses
```


How to use 
```
python tcharai.py character_id 
```
You can get character_id from url https://beta.character.ai/chat?char=M5xMXf4FKepKTYtWPqVaEZzuEuy90uu0eNZr4GZtDsA

or just
```
python tcharai.py
```

To Do
- [x] Wait until character finish typing then send the messages without using time.sleep()
- [ ] New lines support of character message
