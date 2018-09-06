const gulp = require('gulp');

const mjml = require('gulp-mjml');

gulp.task('emails', function() {
  return gulp.src('./accounts/assets/src/mjml/*.mjml')
    .pipe(mjml())
    .pipe(gulp.dest('./accounts/templates/email/'))
});

gulp.task('default', ['emails']);
