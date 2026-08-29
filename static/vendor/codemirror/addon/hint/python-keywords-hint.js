/* Custom Python keyword + builtins autocomplete for CodeMirror 5 */
(function (mod) {
    if (typeof exports === 'object' && typeof module === 'object') mod(exports);
    else if (typeof define === 'function' && define.amd) define(['codemirror'], mod);
    else mod(CodeMirror);
})(function (CodeMirror) {
    var PY_KEYWORDS = [
        'def', 'return', 'print', 'if', 'elif', 'else', 'for', 'while', 'in', 'not',
        'and', 'or', 'True', 'False', 'None', 'import', 'from', 'as', 'try', 'except',
        'finally', 'raise', 'class', 'pass', 'break', 'continue', 'lambda', 'with',
        'yield', 'global', 'nonlocal', 'assert', 'del', 'is', 'range', 'len', 'int',
        'str', 'float', 'list', 'dict', 'set', 'tuple', 'input', 'append', 'sort',
        'sum', 'max', 'min', 'abs', 'round', 'enumerate', 'zip', 'map', 'filter',
        'open', 'format', 'split', 'join', 'replace', 'upper', 'lower', 'strip',
        'items', 'keys', 'values', 'get', 'pop', 'remove', 'insert', 'extend',
        'update', 'clear', 'copy', 'startswith', 'endswith', 'find', 'count'
    ];

    CodeMirror.registerHelper('hint', 'python', function (cm) {
        var cur = cm.getCursor();
        var token = cm.getTokenAt(cur);
        var start = token.start;
        var word = token.string;
        if (/\W/.test(word) && token.type !== 'keyword') return;

        var from = CodeMirror.Pos(cur.line, start);
        var to = CodeMirror.Pos(cur.line, start + word.length);
        var matches = [];

        // Соответствия ключевым словам (префикс)
        var lower = word.toLowerCase();
        for (var i = 0; i < PY_KEYWORDS.length; i++) {
            var kw = PY_KEYWORDS[i];
            if (kw.toLowerCase().startsWith(lower)) {
                matches.push({ text: kw, displayText: kw, className: 'cm-hint-keyword' });
            }
        }

        // Слова уже набранные в документе (любой идентификатор)
        var seen = {};
        cm.eachLine(function (line) {
            var m = line.text.match(/[A-Za-z_][A-Za-z0-9_]*/g);
            if (m) for (var j = 0; j < m.length; j++) {
                var w = m[j];
                if (w.toLowerCase().startsWith(lower) && !seen[w]) {
                    seen[w] = true;
                    matches.push({ text: w, displayText: w });
                }
            }
        });

        return { list: matches, from: from, to: to };
    });
});