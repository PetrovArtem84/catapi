import random

from behave import given, when, then
import requests

from cat_api_vote import CatApiVote

auth_headers = {"x-api-key": "DEMO-API-KEY"}
thecatapi_url = "https://api.thecatapi.com/v1/"


@given('we send get request to thecatapi.com and save the response to the context')
def step_impl(context):
    response = requests.get(thecatapi_url+"votes", headers=auth_headers)
    context.response_code = response.status_code
    context.unmarshaled_list = [CatApiVote(dict_item) for dict_item in response.json()]
    pass


@then('response code is "{response_code}"')
def step_impl(context, response_code):
    assert str(context.response_code) == response_code


@then('response length is more than 0')
def step_impl(context):
    assert len(context.unmarshaled_list) > 0


@when("user randomly selects vote record and saves it to context and gets this record by id")
def step_impl(context):
    context.random_entity = random.choice(context.unmarshaled_list)
    response = requests.get(thecatapi_url+f"votes/{context.random_entity.id}", headers=auth_headers)
    context.response_code = response.status_code
    context.received_entity = CatApiVote(response.json())


@then("response entity is the same as randomly picked")
def step_impl(context):
    assert context.random_entity == context.received_entity


@when('Create a new vote POST /votes. image_id "{image_id}", sub_id "{sub_id}", value "{value}"')
def step_impl(context, image_id, sub_id, value):
    response = requests.post(thecatapi_url + "votes",
                             json= {"image_id": image_id, "sub_id": sub_id, "value": int(value)},
                             headers=auth_headers)

    context.response_code = response.status_code
    context.response_dict = response.json()
    context.created_vote_id = context.response_dict['id']


@then('response "{key}" is "{expected_text}"')
def step_impl(context, key, expected_text):
    if expected_text == 'not empty':
        assert context.response_dict.get(f'{key}') is not None
    else:
        assert context.response_dict[f'{key}'] == expected_text


@when('user gets created record by id')
def step_impl(context):
    response = requests.get(thecatapi_url+f"votes/{context.created_vote_id}", headers=auth_headers)
    context.received_entity = CatApiVote(response.json())
    context.response_code = response.status_code


@then('received vote id matches with created')
def step_impl(context):
    assert context.created_vote_id == context.received_entity.id


@when('user deletes created vote by id')
def step_impl(context):
    response = requests.delete(thecatapi_url+f"votes/{context.created_vote_id}", headers=auth_headers)
    context.response_code = response.status_code
    context.response_dict = response.json()
