var diningHallSelected;
var listofFriends = [];
var dateSelected;
var timeSelected;

$(document).ready(function() {
  $("#notify").click(function(e) {
    window.location = '/notify';
  });

  $(".clickableDiningHalls").click(function(e) {
    diningHallSelected = $(e.currentTarget).data('diningname');
  });

  $(function() {
    $( "#datepicker" ).datepicker();
  });

  $(function() {
    $('#basicExample').timepicker();
  });

  $("#sendToFriends").click(function(e) {
    listofFriends = [];
    var allFriendslist = $('.friendCheckBox');
    for (i=0; i<allFriendslist.length; i++) {
      if (allFriendslist[i].checked) {
        listofFriends.push($(allFriendslist[i]).data('friendname'));
      }
    };

    dateSelected = $('#datepicker').val();
    timeSelected = $('#basicExample').val();

    $.ajax({
      method: "POST",
      url: '/send',
      data: JSON.stringify({'diningHallSelected': diningHallSelected,
              'listofFriends': listofFriends,
              'dateSelected': dateSelected,
              'timeSelected': timeSelected,
            })
      dataType: 'json',
      contentType: "application/json",

          }).done(function(data) {
//
            });
  });



})
