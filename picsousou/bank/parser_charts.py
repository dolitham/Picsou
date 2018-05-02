import json


def round_to_string(value):
    if abs(value) < 1:
        return ""
    return str(round(value))


def add_value(tab, value):
    tab["data"] = tab["data"] + [{"value": round_to_string(value)}]
    return tab


def init_data(name, color):
    data = {}
    data["seriesname"] = name
    data["color"] = color
    data["data"] = []
    return data


def budget_chart_parser(budgets):

    final = {}

    chart = {}
    chart["stack100Percent"] = "1"
    chart["showPercentInTooltip"] = "0"
    chart["showValues"] = "1"
    chart["showPercentValues"] = "0"
    chart["numberPrefix"] = "$"
    chart["borderAlpha"] = "20"
    chart["valueFontColor"] = "#ffffff"
    chart["usePlotGradientColor"] = "0"
    chart["subcaptionFontSize"] = "14"
    chart["showHoverEffect"] = "1"
    chart["showLimits"] = "0"
    chart["showYAxisValues"] = "0"
    final["chart"] = chart

    category = []
    for budget in budgets:
        category.append({"label": budget.name.name})
    categories = {}
    categories["category"] = category
    final["categories"] = [categories]

    data_spent_ok = init_data("spent", "#63aced")
    data_remaining_ok = init_data("remaining", "#7bedae")
    data_spent_over = init_data("spent early", "#0075c2")
    data_remaining_over = init_data("remaining Bonus", "#1aaf5d")
    data_over = init_data("over", "#f2c500")

    for budget in budgets:
        data_spent_ok = add_value(data_spent_ok, budget.spent_ok)
        data_spent_over = add_value(data_spent_over, budget.spent_over)
        data_remaining_ok = add_value(data_remaining_ok, budget.remaining_ok)
        data_remaining_over = add_value(data_remaining_over, budget.remaining_over)
        data_over = add_value(data_over, budget.over)

    final["dataset"] = [data_spent_ok, data_spent_over, data_remaining_over, data_remaining_ok, data_over]

    return json.dumps(final)
