// INSTRUCTIONS: REWRITE THIS IN VANILLA JAVASCRIPT

// $(document).ready(function() {
//
//   // SUBMIT POST FORM
//   $('#post-form').submit(function (e) {
//     e.preventDefault();
//
//     var post = $(this).serialize();
//
//     $.ajax({
//       type: 'POST',
//       url: '/posts',
//       data: post,
//       success: function(data) {
//         $('#posts').prepend(
//           "<div class='list-item'>" +
//             "<p>" + data.title + "</p>" +
//             data.description +
//           "</div>"
//         );
//         // window.location.href = "/posts/" + data._id
//       },
//       error: function(err) {
//         console.log(err);
//       }
//     });
//   });
//
// });
