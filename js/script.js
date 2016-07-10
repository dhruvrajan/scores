$(document).ready(function() {
  var hidden = ['#step2', '#step3'];
  for (var i = 0; i < hidden.length; i++) {
    $(hidden[i]).hide();
  }
  $('#ap-button').click(function() {
    var text = 'Advanced Placement';
    var data = JSON.parse(apJSON);
    $('#test-header').text('Enter ' + text + ' scores');
    for (var i = 0; i < data.length; i++) {
      $('#test-name-select').append('<option>' + data[i]['name'] + '</option>');
    }
    for (var i = 0; i < 5; i++) {
      $('#test-score-select').append('<option>' + (i + 1) + '</option>');
    }
    $('#step2').show();
    $('#test-add').click(function() {
      var name = $('#test-name-select').find('option:selected').text();
      var score = $('#test-score-select').find('option:selected').text();
      $('#test-table tbody').append(
        '<tr><td>' + name +
        '</td><td>' + score +
        '</td></tr>'
      );
    });
    $('#test-submit').click(function() {
      var serialized = [];
      var entries = $('#test-table tbody tr');
      $('#results-table tbody').empty();
      for (var i = 0; i < entries.length; i++) {
        let raw = $(entries[i]).find($('td'));
        let name = $(raw[0]).text();
        let score = $(raw[1]).text();
        serialized.push({'name': name, 'score': score});
      }
      for (var i = 0; i < serialized.length; i++) {
        serialized[i]['course'] = 'None';
        for (var j = 0; j < data.length; j++) {
          if (serialized[i]['name'] === data[j]['name']) {
            let score = serialized[i]['score'];
            if (data[j].hasOwnProperty(score)) {
              serialized[i]['course'] = data[j][score];
            }
          }
        }
        $('#results-table tbody').append(
          '<tr><td>' + serialized[i]['name'] +
          '</td><td>' + serialized[i]['score'] +
          '</td><td>' + serialized[i]['course'] +
          '</td></tr>'
        );
      }
      $('#step3').show();
    });
  });
});
