// Tab Functionality
// jQuery(document).ready(function() {
//     jQuery('.tabs .tab-links a').on('click', function(e)  {
//         var currentAttrValue = jQuery(this).attr('href');
//
//         // Show/Hide Tabs
//         jQuery('.tabs ' + currentAttrValue).fadeIn(400).siblings().hide();
//
//         // Change/remove current tab to active
//         jQuery(this).parent('li').addClass('active').siblings().removeClass('active');
//
//         e.preventDefault();
//     });
// });

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
