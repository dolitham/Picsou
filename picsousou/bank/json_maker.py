import json


def to_str(value):
    if abs(value) < 1:
        return ""
    return str(round(value))


def append_value(tab, value):
    tab["data"] = tab["data"] + [{"value": to_str(value)}]
    return tab


def json_maker(budgets):

    final = {}

    chart = {}
    chart["stack100Percent"] = "1"
    chart["showPercentInTooltip"] = "0"
    chart["showValues"] = "1"
    chart["showPercentValues"] = "0"
    chart["numberPrefix"] = "$"
    chart["bgColor"] = "#ffffff"
    chart["borderAlpha"] = "20"
    chart["valueFontColor"] = "#ffffff"
    chart["usePlotGradientColor"]="0"
    chart["divlineColor"] = "#999999"
    chart["divLineDashed"] = "1"
    chart["showAlternateHGridColor"] = "0"
    chart["subcaptionFontBold"] = "0"
    chart["subcaptionFontSize"] = "14"
    chart["showHoverEffect"] = "1"
    chart["showLimits"] = "0"
    chart["showYAxisValues"] = "0"

    final["chart"] = chart

    category = []
    for budget in budgets:
        category.append({"label":budget.name.name})
    categories = {}
    categories["category"] = category
    final["categories"] = [categories]

    dataset_spent_ok = {}
    dataset_spent_ok["seriesname"] = "spent"
    dataset_spent_ok["color"] = "#63aced"
    dataset_spent_ok["data"] = []

    dataset_remaining_ok = {}
    dataset_remaining_ok["seriesname"] = "remaining"
    dataset_remaining_ok["color"] = "#7bedae"
    dataset_remaining_ok["data"] = []

    dataset_spent_over = {}
    dataset_spent_over["seriesname"] = "spent early"
    dataset_spent_over["color"] = "#0075c2"
    dataset_spent_over["data"] = []

    dataset_remaining_over = {}
    dataset_remaining_over["seriesname"] = "remaining Bonus"
    dataset_remaining_over["color"] = "#1aaf5d"
    dataset_remaining_over["data"] =  []

    dataset_over = {}
    dataset_over["seriesname"] = "over"
    dataset_over["color"] = "#f2c500"
    dataset_over["data"] = []

    for budget in budgets:
        print(budget.name)
        spent = budget.spent

        theoretical_spending = budget.theoretical_spending
        theoretical_remaining = budget.prevision - theoretical_spending
        spent_ok = min(spent, theoretical_spending)
        spent_over = spent - spent_ok
        remaining = budget.remaining
        remaining_over = max(remaining - theoretical_remaining, 0)
        remaining_ok = remaining - remaining_over
        print('theo', theoretical_spending, 'spent', spent, 'rem', remaining)

        dataset_spent_ok = append_value(dataset_spent_ok, spent_ok)
        dataset_spent_over = append_value(dataset_spent_over, spent_over)
        dataset_remaining_ok = append_value(dataset_remaining_ok, remaining_ok)
        dataset_remaining_over = append_value(dataset_remaining_over, remaining_over)
        dataset_over = append_value(dataset_over, budget.over)

    final["dataset"] = [dataset_spent_ok, dataset_spent_over, dataset_remaining_over, dataset_remaining_ok, dataset_over]


    return json.dumps(final)

