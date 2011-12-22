from django.core import serializers
import json

class Japi:
	"""API simple responder class"""

	response = { 'status': 'ok', 'action':'' }
    
	def __init__( self, action ):
		self.response[ 'action' ] = action
		if not hasattr( self, action ):
			self.response[ 'status' ] = "ko"
			self.response[ 'error'] = action + " not found!"
		else:
			func = getattr( self, action )			
			func()
	
	def __str__( self ):
		return json.dumps( self.response )	

	def help( self ):
		self.response[ 'available_methods' ] = {
			'help':'this action, provide some basic snippets'
		}

		
