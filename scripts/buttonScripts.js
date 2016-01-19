var diningHallSelected;
var listofFriends = [];

$(document).ready(function() {
  $("#notify").click(function(e) {
    window.location = '/notify';
  });

  $(".clickableDiningHalls").click(function(e) {
    diningHallSelected = $(e.currentTarget).data('diningname');
  });

  $("#sendToFriends").click(function(e) {
    listofFriends = [];
    var allFriendslist = $('.friendCheckBox');
    console.log(allFriendslist);
    for (i=0; i<allFriendslist.length; i++) {
      if (allFriendslist[i].checked) {
        listofFriends.push($(allFriendslist[i]).data('friendname'));
      }
    };
    console.log(listofFriends);

  });



})
