// Function to add tab functionality on page

function openTab(evt, tabName, section) {
  var i, tabcontent, tablinks;

  tabcontent = document.getElementsByClassName('tabcontent' + section);
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablinks" + section);
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";

}


// Mouse over picture funtionality for our team
