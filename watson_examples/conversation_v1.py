import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
    username='c4129348-b14c-4d2d-80ca-25b1acc59ca7',
    password='dHfhKbO2pXH4',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = 'b42ee794-c019-4a0d-acd2-9e4d1d016767'

response = conversation.message(workspace_id=workspace_id, message_input={'text': 'What\'s the weather like?'})
print(json.dumps(response, indent=2))

# When you send multiple requests for the same conversation, include the context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))
