# Autogenerated file
def render(req):
    yield """<html>
Request path: '"""
    yield str(req.path)
    yield """'<br>
<table border=\"1\">
"""
    for i in range(5):
        yield """<tr><td> """
        yield str(i)
        yield """ </td><td> """
        yield str("%2d" % i ** 2)
        yield """ </td></tr>
"""
    yield """</table>
</html>
"""
