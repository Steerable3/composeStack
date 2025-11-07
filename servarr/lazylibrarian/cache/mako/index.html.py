# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1762071045.7323587
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = ['headerIncludes', 'body', 'javascriptIncludes']



import lazylibrarian
from lazylibrarian.config2 import CONFIG


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        pref = context.get('pref', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div id="subhead_container" class="row">\n      <form action="search" method="get">\n        <div id="subhead_menu"  class="col-xs-12 col-md-8">\n')
        if perm&lazylibrarian.perm_force:
            __M_writer('            <a href="force_update" class="btn btn-sm btn-primary" id="refresh"><i class="fa fa-sync"></i> Refresh Authors</a>\n')
        if lazylibrarian.IGNORED_AUTHORS == True:
            __M_writer('              <a href="toggle_auth" class="button btn btn-sm btn-primary"><i class="fa fa-user"></i> Show Active Authors</a>\n')
        else:
            __M_writer('              <a href="toggle_auth" class="button btn btn-sm btn-primary"><i class="fa fa-user-secret"></i> Show Inactive Authors</a>\n')
        if CONFIG['USER_ACCOUNTS']:
            pass
            if pref&lazylibrarian.pref_myauthors:
                __M_writer('                <a href="toggle_my_auth" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="All, or just mine"><i class="fa fa-user-circle"></i></a>\n')
            else:
                __M_writer('                <a href="toggle_my_auth" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="All, or just mine"><i class="fa fa-users"></i></a>\n')
        if lazylibrarian.IGNORED_AUTHORS == True:
            __M_writer('                <a href="author_wall?have=0" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="Grid view"><i class="fa fa-th"></i></a>\n')
        else:
            __M_writer('                <a href="author_wall?have=1" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="Grid view"><i class="fa fa-th"></i></a>\n')
        if CONFIG['CONTRIBUTING_AUTHORS']:
            pass
            if lazylibrarian.PRIMARY_AUTHORS == True:
                __M_writer('                    <a href="toggle_primary" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="Primary Author, or All Contributors"><i class="fa fa-star"></i></a>\n')
            else:
                __M_writer('                    <a href="toggle_primary" class="button btn btn-sm btn-primary" data-toggle="tooltip" title="Primary Author, or All Contributors"><i class="fa fa-handshake"></i></a>\n')
        __M_writer('        </div>\n        <div class="clearfix visible-xs"><hr/></div>\n')
        if perm&lazylibrarian.perm_search:
            __M_writer('        <div class="col-xs-12 col-md-4">\n        <div class="form-group">\n          <label class="sr-only">Search</label>\n          <div class="input-group">\n            <input type="search" id="searchfor" name="searchfor" placeholder="Title / Author / ISBN" class="form-control input-sm col-xs-12">\n            <span class="input-group-btn">\n              <button type="submit" id="btnsearch" name="btnsearch" onclick="reveal();" value="index" class="btn btn-sm btn-primary" data-toggle="tooltip" data-placement="bottom" title="Search for author/book"><i class="fa fa-search"></i></button>\n            </span>\n          </div>\n        </div>\n        </div>\n')
        __M_writer('      </form>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n')
        if lazylibrarian.AUTHORS_UPDATE == 1:
            __M_writer('    <p>\n    <button onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Author Refresh in progress ...</button>\n    </p>\n')
        else:
            pass
            if lazylibrarian.SEARCHING == 1:
                __M_writer('      <p>\n      <button onclick="" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Search in progress ...</button>\n      </p>\n')
            else:
                __M_writer('      <p>\n      <button onclick="" class="hidden" id="myAlert" title=""><i class="fa fa-circle-notch fa-spin"></i> Search in progress ...</button>\n      </p>\n')
        __M_writer('\n<form name="mark_authors" id="mark_authors" action="mark_authors" method="get" class="form-inline" onsubmit="return false;">\n  <div class="row">\n')
        if perm&lazylibrarian.perm_status or CONFIG['USER_ACCOUNTS']:
            __M_writer('      <div class="col-xs-12 col-sm-5">\n          <div class="form-group">\n            <label for="mark_authors" class="control-label">Mark selected as</label>\n            <select class="mark_authors form-control input-sm" id="action" name="action">\n')
            if perm&lazylibrarian.perm_status:
                __M_writer('              <option value="Active">Active</option>\n              <option value="Wanted">Wanted</option>\n              <option value="Ignored">Ignored</option>\n              <option value="Paused">Paused</option>\n              <option value="Remove">Remove</option>\n              <option value="Delete">Delete</option>\n')
            if CONFIG['USER_ACCOUNTS']:
                __M_writer('                <option value="Subscribe">Subscribe</option>\n                <option value="Unsubscribe">Unsubscribe</option>\n')
            __M_writer('            </select>\n          </div>\n          <button type="submit" class="btn btn-sm btn-primary" onclick="validateForm()">Go</button>\n      </div>\n')
        if CONFIG['TOGGLES']:
            __M_writer('      <div class="toggles col-xs-12 col-sm-7 text-right">\n        Toggle: <a class="toggle-vis" data-column="1"> Image</a>\n        <a class="toggle-vis" data-column="2"> Author</a>\n        <a class="toggle-vis" data-column="3"> Added</a>\n        <a class="toggle-vis" data-column="4"> Latest</a>\n        <a class="toggle-vis" data-column="5"> Released</a>\n        <a class="toggle-vis" data-column="6"> Downloaded</a>\n        <a class="toggle-vis" data-column="7"> Status</a>\n      </div>\n')
        __M_writer('  </div>\n  <br/>\n  <div class="table-responsive">\n    <table class="display table table-striped table-hover table-bordered" id="author_table">\n      <thead>\n        <tr>\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('            <th class="select text-center no-sort"><input type="checkbox" id="allcheck" onClick="toggleAll(this)" /></th>\n')
        else:
            __M_writer('            <th class="hidden"></th>\n')
        __M_writer('          <th class="authorimg no-sort">Image</th>\n          <th class="authorname">Author</th>\n          <th class="date text-center">Added</th>\n          <th class="bookname">Latest Book</th>\n          <th class="date text-center">Released</th>\n          <th class="have text-center">Downloaded</th>\n          <th class="status text-center">Status</th>\n        </tr>\n      </thead>\n    </table>\n  </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        perm = context.get('perm', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <script type="text/javascript">\n\n    function reveal() {\n        var searchval = document.getElementById("searchfor").value;\n            if (Boolean(searchval) == true) {\n                $(\'#myAlert\').removeClass(\'hidden\');\n            }\n    };\n\n    function reason(target) {\n        window.alert(target);\n    };\n\n    $(document).ready(function()\n    {\n        var selected = [];\n        var intjob = 0;\n\n        var input = document.getElementById("searchfor");\n        input.addEventListener("keypress", function(event) {\n            if (event.key === "Enter") { reveal(); }\n        });\n\n        $(\'input.deletable\').wrap(\'<span class="deleteicon" />\').after($(\'<span/>\').click(function() {\n            $(this).prev(\'input\').val(\'\').trigger(\'change\').focus();\n        }));\n\n        var table = $(\'#author_table\').DataTable(\n            {\n                "dom": "<\'row\'<\'col-xs-6\'l><\'col-xs-6\'f>><\'row\'<\'col-sm-12\'tr>><\'row\'<\'col-sm-5\'i><\'col-sm-7\'p>>",\n                "responsive": true,\n                "bAutoWidth": false,\n                "stateSave": true,\n                "order": [[ 2, \'asc\']],\n                "rowId": 10,\n                "displayStart": 0,\n                "columnDefs":\n                    [{ targets: \'no-sort\', orderable: false },\n                      { targets: [0],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                            if ( $.inArray("I" + row[10], selected) !== -1 ) {\n                                return \'<input type="checkbox" id="I\' + row[10] + \'" name="\' + row[10] + \'" class="checkbox" checked=true />\'; }\n                            return \'<input type="checkbox" id="I\' + row[10] + \'" name="\' + row[10] + \'" class="checkbox" />\';} },\n                     { targets: [1],\n                         \'render\': function(data, type, row) {\n                            return \'<a href="\' + row[0] + \'" target="_blank" rel="noreferrer"><img src="\' + row[0] + \'" alt="Cover" class="bookcover-sm"></a>\';} },\n                     { targets: [2], \'render\': function(data, type, row) {\n')
        if perm&lazylibrarian.perm_authorbooks:
            __M_writer('                        btn = \'<a href=\\\'author_page?authorid=\' + row[10] + \'\\\'">\' + row[1] + \'</a>\'\n')
        else:
            __M_writer("                        btn = '<a>' + row[1] + '</a>'\n")
        __M_writer('                     return btn ;}\n                     },\n                     { targets: [3],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                            return \'<a data-toggle="tooltip" title="\' + row[14] + \'">\' + row[13] + \'</a>\';} },\n                     { targets: [4], \'render\': function(data, type, row) {\n                        if (row[2] == null) {return \'\'};\n                            return \'<button onclick="bookinfo(\\\'\' + row[11] +\n                                \'\\\')" class="button btn-link text-left" type="button">\' + row[2] + \'</button>\';} },\n                     { targets: [5],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                            return row[3];} },\n                     { targets: [6],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n                        var have = +row[8] || 0;\n                        var tot = +row[9] || 0;\n                        var percent = (have * 100 / tot);\n                        if (percent <= 25) {css = \'danger\'}\n                        else if (percent <= 50) {css = \'warning\'}\n                        else if (percent <= 75) {css = \'info\'}\n                        else {css = \'success\'};\n                        bar = \'<div class="progress center-block" style="width: 120px;"><div class="progress-bar-\' +\n                        css + \' progress-bar progress-bar-striped" role="progressbar" aria-valuenow="\' + percent +\n                        \'" aria-valuemin="0" aria-valuemax="100" style="width: \' + percent +\n                        \'%;"><span class="sr-only">\' + percent +\n                        \'% Complete</span><span class="progressbar-front-text">\' + have + \'/\' + tot +\n                        \'</span></div></div>\';\n                        return bar;} },\n                     { targets: [7],\n                        \'class\': \'text-center\',\n                        \'render\': function(data, type, row) {\n')
        if perm&lazylibrarian.perm_status:
            __M_writer('                            bar = \'<button onclick="reason(\\\'\' + row[14] +\n                            \'\\\')" class="button btn btn-xs btn-primary" type="button">\' + row[5] +\n                            \'</button>\';\n')
        else:
            __M_writer('                            bar = row[5];\n')
        __M_writer('                          return bar;} },\n                     { type: \'natural-nohtml\', targets: [3,5] }],\n                "oLanguage": {\n                    "sSearch": "Filter: ",\n                    "sLengthMenu":"_MENU_ rows per page",\n                    "sEmptyTable": "No authors found",\n                    "sInfo":"Showing _START_ to _END_ of _TOTAL_ rows",\n                    "sInfoEmpty":"Showing 0 to 0 of 0 rows",\n                    "sInfoFiltered":"(filtered from _MAX_ total rows)"},\n                "bServerSide": true,\n                "sAjaxSource": \'get_index\',\n                "bFilter": true,\n                "aLengthMenu": [[5, 10, 15, 25, 50, 100, 500, 1000, 5000, -1], [5, 10, 15, 25, 50, 100, 500, 1000, 5000, "All"]],\n                "iDisplayLength": ')
        __M_writer(str(CONFIG['DISPLAYLENGTH']))
        __M_writer(',\n                "sPaginationType": "full_numbers",\n                "fnRowCallback": function (nRow, aData, iDisplayIndex, iDisplayIndexFull) {\n')
        if perm&lazylibrarian.perm_status == 0:
            __M_writer('                      $(\'td\', nRow).eq(0).addClass("hidden");\n')
        __M_writer('                    return nRow;\n                },\n                "aaSorting": [[2, \'asc\']],\n            });\n\n          $(\'#author_table tbody\').on(\'click\', \'tr input:checkbox\', function () {\n              var id = this.id;\n              var index = $.inArray(id, selected);\n              if ( index === -1 ) {\n                  selected.push( id );\n              } else {\n                  selected.splice( index, 1 );\n              }\n              $(this).toggleClass(\'selected\');\n          } );\n\n            table.on( \'xhr\', function () {\n              var json = table.ajax.json();\n              if (json.loading || json.searching) {\n                if (intjob === 0) {\n                  intjob = setInterval( function () {\n                    table.ajax.reload( null, false );\n                    }, 10000 );\n                }\n              }\n              else {\n                if (intjob != 0) { clearInterval( intjob )};\n                $(\'#myAlert\').addClass(\'hidden\');\n              };\n            });\n\n        $(\'.dataTables_filter input\').attr("placeholder", "Results filter");\n        $(\'a.toggle-vis\').click(function (e) {\n            e.preventDefault();\n            var column = table.column( $(this).attr(\'data-column\') );\n            column.visible( ! column.visible() );\n        } );\n    });\n\n\n    function validateForm() {\n        var x = document.forms["mark_authors"]["action"].value;\n        var c = ($(":checkbox:checked").length);\n        var all_check = document.getElementById("allcheck").checked;\n        if (all_check) { c -= 1};\n        if (c > 0 && (x == "Delete" || x == "Remove")) {\n            if (x == "Delete") {\n                if (c == 1){ msg = "Are you sure you want to permanently delete the selected author and their books?"}\n                if (c > 1){ msg = "Are you sure you want to permanently delete the " + c +\n                            " selected authors and their books?"}\n                };\n            if (x == "Remove") {\n                if (c == 1){ msg = "Are you sure you want to remove the selected author?"}\n                if (c > 1){ msg = "Are you sure you want to remove the " + c + " selected authors?"}\n                };\n            bootbox.confirm({\n                message: msg,\n                buttons: {\n                    confirm: {\n                        label: \'Yes\',\n                        className: \'btn-success\'\n                    },\n                    cancel: {\n                        label: \'No\',\n                        className: \'btn-danger\'\n                    }\n                },\n                callback: function (result) {\n                    if (result) { submitFormAjax(); }\n                }\n            });\n            return false;\n        }\n        else { submitFormAjax(); }\n    }\n\n    function bookinfo(bookid) {\n        $.get(\'bookdesc\', {\'bookid\': bookid},\n        function(data) {\n            var $textAndPic = $(\'<div></div>\');\n            $textAndPic.append(\'<img src="./cache/book/\' + bookid + \'.jpg" />\');\n            var res = data.split(\'^\');\n            var title = res[0]\n            var desc = res[1]\n            $textAndPic.append(\'<br>\' + desc + \' <br />\');\n            bootbox.dialog({\n                size: "large",\n                title: title,\n                message: $textAndPic,\n                buttons: {\n                   primary: {\n                        label: "Close",\n                        className: \'btn-primary\'\n                    }\n                }\n            });\n        });\n    };\n\n    var timer = 2000;\n    if( timer > 0 )\n        {\n            tm = setInterval( function () {\n                $.get(\'libraryscan_progress\', function (data) {\n                    $("#myAlert").html(data);\n            });\n            }, timer );\n        }\n\n    function submitFormAjax() {\n        var form = document.getElementById("mark_authors");\n        var formData = new FormData(form);\n\n        // Show loading modal\n        bootbox.dialog({\n            message: \'<div class="text-center"><i class="fa fa-spinner fa-spin fa-2x"></i><br><br>Processing...</div>\',\n            size: \'small\',\n            backdrop: false,\n            closeButton: false\n        });\n\n        // Convert FormData to URLSearchParams for the AJAX call\n        var params = new URLSearchParams();\n        var formDataEntries = formData.entries();\n        for (var pair of formDataEntries) {\n            params.append(pair[0], pair[1]);\n        }\n\n        // Make AJAX call to the new endpoint\n        fetch(\'mark_authors_ajax\', {\n            method: \'POST\',\n            headers: {\n                \'Content-Type\': \'application/x-www-form-urlencoded\',\n            },\n            body: params\n        })\n        .then(response => response.json())\n        .then(data => {\n            // Close loading modal\n            bootbox.hideAll();\n\n            // Show result modal\n            var message = \'<div class="alert alert-info"><strong>Summary:</strong><br>\' + data.summary + \'</div>\';\n            if (data.passed > 0 || data.failed > 0) {\n                message += \'<div class="row">\';\n                message += \'<div class="col-md-6"><span class="label label-success">Successful: \' + data.passed + \'</span></div>\';\n                if (data.failed > 0) {\n                    message += \'<div class="col-md-6"><span class="label label-danger">Failed: \' + data.failed + \'</span></div>\';\n                }\n                message += \'</div>\';\n            }\n            bootbox.dialog({\n                title: \'Mark Authors Complete\',\n                message: message,\n                buttons: {\n                    ok: {\n                        label: \'OK\',\n                        className: \'btn-primary\',\n                        callback: function() {\n                            window.location.reload();\n                        }\n                    }\n                }\n            });\n        })\n        .catch(error => {\n            // Close loading modal\n            bootbox.hideAll();\n\n            // Show error modal\n            bootbox.dialog({\n                title: \'Error\',\n                message: \'<div class="alert alert-danger">An error occurred: \' + error.message + \'</div>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\',\n                            callback: function(result){ window.location.reload(\'series\'); }\n                        },\n                    }\n            });\n        });\n    }\n  </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"16": 2, "17": 3, "18": 4, "19": 5, "20": 6, "32": 0, "37": 1, "38": 5, "39": 54, "40": 132, "41": 431, "47": 6, "53": 6, "54": 10, "55": 11, "56": 13, "57": 14, "58": 15, "59": 16, "60": 18, "62": 19, "63": 20, "64": 21, "65": 22, "66": 25, "67": 26, "68": 27, "69": 28, "70": 30, "72": 31, "73": 32, "74": 33, "75": 34, "76": 37, "77": 39, "78": 40, "79": 52, "85": 56, "91": 56, "92": 57, "93": 57, "94": 58, "95": 59, "96": 62, "98": 63, "99": 64, "100": 67, "101": 68, "102": 73, "103": 76, "104": 77, "105": 81, "106": 82, "107": 89, "108": 90, "109": 93, "110": 98, "111": 99, "112": 109, "113": 115, "114": 116, "115": 117, "116": 118, "117": 120, "123": 133, "128": 133, "129": 182, "130": 183, "131": 184, "132": 185, "133": 187, "134": 221, "135": 222, "136": 225, "137": 226, "138": 228, "139": 241, "140": 241, "141": 244, "142": 245, "143": 247, "149": 143}}
__M_END_METADATA
"""
