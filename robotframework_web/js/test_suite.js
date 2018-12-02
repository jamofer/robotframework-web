const TEST_SUITE = (test_suite) => `
<div id="${test_suite.id}" class="card test_suite">
    <div class="card-header" data-toggle="collapse">
        <span class="badge badge-pill badge-primary">SUITE</span> ${test_suite.name}
    </div>
    <div class="card-body test_suite_body">
    </div>
</div>
`;

const TEST_CASE = (test_case) => `
<div id="${test_case.id}" class="card test_case">
    <div class="card-header" data-toggle="collapse">
        <span class="badge badge-pill badge-primary">TEST</span> ${test_case.name}
    </div>
    <div class="card-body test_case_body">
    </div>
</div>
`;

const KEYWORD = (keyword) => `
<div id="${keyword.id}" class="card keyword">
    <div class="card-header" data-toggle="collapse">
        <span class="badge badge-pill badge-primary">KEYWORD</span> ${keyword.name}
    </div>
    <div class="card-body keyword_body">
    </div>
</div>
`;


const MESSAGE = (message) => `
<div class="card message">
    <div class="card-header" data-toggle="collapse">
        ${message.message}
    </div>
</div>
`;

function create_test_suite(test_suite) {
    $('#current').append(TEST_SUITE(test_suite))
}

function append_test_suite(test_suite, target) {
    $(`#${target} .test_suite_body`).append(TEST_SUITE(test_suite))
}

function append_test_case(test_case, target) {
    $(`#${target} .test_suite_body`).append(TEST_CASE(test_case))
}

function append_keyword(keyword, target) {
    $(`#${target} .card-body:first`).append(KEYWORD(keyword))
}

function append_message(message, target) {
    $(`#${target} .keyword_body`).append(MESSAGE(message))
}