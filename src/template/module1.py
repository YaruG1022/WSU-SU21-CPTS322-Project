
from flask import Flask, render_template, url_for, request


app = Flask(__name__, template_folder='src/templates')

@app.route('/')
@app.route('/p1')
def p1():
    return render_template("homepage.html", tittle="Template")


@app.route('/p2',method =['POST'])
def p2():
    output=request.form.to_dict()
    print(output)
    project = output["project"]
    return render_template("HtmlPage2.html", python_project_data = project)


@app.route('/p3', method = ['POST'])
def p3():
    output=request.form.to_dict()
    print(output)
    inventory = output["inventory"]
    return render_template("HtmlPage3.html", python_inventory_data = inventory)

@app.route('/p4', method = ['POST', 'GET'])
def p4():

    return render_template("HtmlPage4.html", tittle="Template")


@app.route('style')
def style():
    return render_template("StyleSheet.css")


if __name__ == "__main__":
    app.run(debug=True)


