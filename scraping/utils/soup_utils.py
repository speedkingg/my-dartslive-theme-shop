# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


class soup_utils:
    def __init__(self):
        pass

    def get_souped_html(self, session, html):
        """
        BeautifulSoupでhtmlをsoupして返す

        Parameters
        ----------
        session:
            現在使用しているsessionの参照渡し

        html : string
            ページのhtml

        Return
        ----------
        html: string
            BeautifulSoupでsoupされたHTML

        """
        res = session.get(html)
        res.raise_for_status()  # エラーならここで例外を発生させる

        # UnicodeEncodeError[cp932]回避
        html = res.text.encode('cp932', "ignore").decode('cp932')

        return BeautifulSoup(html, "html.parser")
