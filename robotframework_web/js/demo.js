suite1 = {
    id: 'ts1',
    name: 'Suite 1'
}

subsuite1 = {
    id: 'tss1',
    name: 'SubSuite 1'
}

suite2 = {
    id: 'ts2',
    name: 'Suite 2'
}

test_case = {
    id: 'tc1',
    name: 'Test Case 1'
}

keyword1 = {
    id: 'kw1',
    name: 'Do not sell beer in the world'
}

keyword2 = {
    id: 'kw2',
    name: 'Wait for WW3'
}

keyword3 = {
    id: 'kw3',
    name: 'Tear down'
}

keyword4 = {
    id: 'kw4',
    name: 'Reset World'
}

message = {
    message: 'Test message'
}

$(function()
{
    create_test_suite(suite1);
    append_test_suite(subsuite1, suite1.id);
    create_test_suite(suite2);

    append_test_case(test_case, subsuite1.id);
    append_keyword(keyword1, test_case.id);
    append_keyword(keyword2, test_case.id);
    append_keyword(keyword3, test_case.id);
    append_keyword(keyword4, keyword3.id);

    append_message(message, keyword1.id)
    append_message(message, keyword1.id)
    append_message(message, keyword1.id)

    append_message(message, keyword2.id)

    append_message(message, keyword4.id)
});