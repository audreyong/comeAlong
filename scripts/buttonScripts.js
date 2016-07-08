var diningHallSelected;
var listofFriends = [];
var dateSelected;
var timeSelected;

$(document).ready(function() {
  $("#notify").click(function(e) {
    window.location = '/notify';
  });

  //hide date and time and friends list div
   $("#dateAndTime").hide();
   $("#friendsList").hide();

  $(".clickableDiningHalls").click(function(e) {
    diningHallSelected = $(e.currentTarget).data('diningname');
     $("#diningHallList").hide();//hide the dining div
      $("#dateAndTime").show();
  });

//date and timepicker classes through jQuery UI
  $(function() {
    $( "#datepicker" ).datepicker();
  });

  $(function() {
    $('#basicExample').timepicker();
  });

  $("#addFriends").click(function(e) {
    window.location.replace('/addFriends');
  });

// hide date and time picker
  $("#nextFromDateAndTime").click(function(e) {
     $("#dateAndTime").hide();
     $("#friendsList").show();
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
            }),
      dataType: 'json',
      contentType: "application/json",

          }).done(function(data) {
//
            });
    //$("#friendsList").hide( "fade", { direction: "down" }, "fast" );
  });



})
