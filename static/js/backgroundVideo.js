var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    height: '100%',
    width: '100%',
    playerVars: {
      autoplay: 1,
      loop: 1,
      controls: 0,
      showinfo: 0,
      autohide: 0,
      modestbranding: 1,
      vq: 'hd720'},
   videoId: 'sxH7hU-WXng',
   events: {
     'onReady': onPlayerReady,
     'onStateChange': onPlayerStateChange
   }
  });
}

function onPlayerReady(event) {
  event.target.playVideo();
  player.mute();
}

var done = false;
function onPlayerStateChange(event) {
  event.target.playVideo();
  player.mute();
}

// function stopVideo() {
//   player.stopVideo();
// }
