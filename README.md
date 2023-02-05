# tcharai
A TUI script for interacting with CharacterAI using Python
![](https://github.com/niizam/tcharai/blob/main/tcharai.gif)
Install requirements
```
pip install playwright
playwright install firefox
```


How to use (for example: python tcharai.py https://beta.character.ai/chat?char=zb7I4U9OYfewmEgOWLBHScefPeELkm1J-_GZDjHLY1M )
```
python tcharai.py [url] 
```
or just
```
python tcharai.py
```

To Do
- [x] Wait until character finish typing then send the messages without using time.sleep()
- [ ] New lines support of character message
