from typing  import Callable,Dict,Any,Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
class IsadminMiddlaware(BaseMiddleware):
	"""docstring for ClassName"""
	def __call__(
		self,
		handler:Callable[[Message, Dict[str,Any]], Awaitable[Any]],
		event:Message,
		data:Dict[str,Any]
		) -> Any:
		user = event.from_user