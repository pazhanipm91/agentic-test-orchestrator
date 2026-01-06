def confidence_score(llm_analysis: str) -> float:
    score = 1.0

    if "timeout" in llm_analysis.lower():
        score -= 0.2
    if "flaky" in llm_analysis.lower():
        score -= 0.3
    if "assertion" in llm_analysis.lower():
        score -= 0.1

    return round(max(score, 0.0), 2)
