from agents.confidence_scorer import confidence_score
from agents.failure_analyzer import analyze_failure

MAX_RETRIES = 3
CONFIDENCE_THRESHOLD = 0.6

def execute_with_retry(run_test, regenerate_test):
    for attempt in range(MAX_RETRIES):
        result = run_test()

        if result.passed:
            return result

        analysis = analyze_failure(
            result.test_name,
            result.request,
            result.response,
            result.error
        )

        confidence = confidence_score(analysis)

        if confidence < CONFIDENCE_THRESHOLD:
            regenerate_test(analysis)
        else:
            break

    return result
