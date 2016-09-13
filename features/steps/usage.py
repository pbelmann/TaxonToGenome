from behave import *
import database_request
import os.path


@given('the output directory exists')
def given_output_exists(context):
    os.makedirs(os.path.join(context._config.base_dir, "output"),  exist_ok=True)
    assert True


@when('I run database request with the commands "{text}"')
def when_database_request(context, text):
    words = [os.path.join(context._config.base_dir, word)
             if word.startswith("input") or word.startswith("output") else word for word in text.split(" ")]
    database_request.main(words)


@then('the following files should be available')
def available_files(context):
    base_dir = context._config.base_dir
    files = context.text.split("\n")
    any(filter(lambda path: os.path.exists(path), map(lambda path: os.path.join(base_dir, path), files)))