from urllib import parse as p


def parse(query: str) -> dict:
    values = p.urlsplit(query).query
    data = dict(p.parse_qsl(values))
    return data


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    assert parse('https://example.com/sometest1/test1?someValue1=value1') == {'someValue1': 'value1'}
    assert parse('https://example.com/sometest12/test2/test?one=1') == {'one': '1'}
    assert parse('http://example.com/sometest3/test/test1?boolean=True') == {'boolean': 'True'}
    assert parse('http://example.com/test4name/?name=someName') == {'name': 'someName'}
    assert parse('http://example.com/sometest5/test5/test5/test5/?test==') == {'test': '='}

    assert parse('https://example.com/path/to/page?value1=1') == {'value1': '1'}
    assert parse('https://example.com/path/to/page?value1=1&value2=2') == {'value1': '1', 'value2': '2'}
    assert parse('http://example.com/?value1=1&value2=v2&value3=False') == {'value1': '1', 'value2': 'v2', 'value3': 'False'}
    assert parse('http://example.com/?value4=7') == {'value4': '7'}
    assert parse('http://example.com/?name=Jerax') == {'name': 'Jerax'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
