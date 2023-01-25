from playwright.sync_api import Playwright, sync_playwright, expect
import curses
import sys
import time
import datetime

def run(stdscr):
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "https://beta.character.ai/chat?char=Dz6sI1u_P8LRwpMPHKa70C8JGJIfqMpqDmJ_s8sw8HE"
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.get_by_role("button", name="I understand").click()

    while True:
        stdscr.refresh()
        stdscr.addstr("> ")
        stdscr.refresh()
        curses.echo()
        now = datetime.datetime.now()
        time_str = "[{:%H:%M}]".format(now)
        message = stdscr.getstr().decode()
        page.get_by_placeholder("Type a message").fill(message)
        page.get_by_placeholder("Type a message").press("Enter")
        chara = page.query_selector('div.chattitle.p-0.pe-1.m-0')
        chara_name = chara.inner_text()
        time.sleep(20)
        div = page.query_selector('div.msg.char-msg')
        output_text = div.inner_text()
        stdscr.addstr(time_str+ chara_name + ' ✉\n' + output_text + '\n \n')
        stdscr.refresh()
        if stdscr.getch() == 27:
            break

    context.close()
    browser.close()

if __name__ == '__main__':
    with sync_playwright() as playwright:
        curses.wrapper(run)
