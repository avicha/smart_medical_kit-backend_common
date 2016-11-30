# coding=utf-8
from base import BaseEvent
import sys
import traceback


class UncaughtErrorEvent(BaseEvent):

    def handle(self, sender, e):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        return e.__class__.__name__
