'use strict';

var gulp = require('gulp');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');
var spawn = require('child_process').spawn;

gulp.task('build-minify-css', function() {
	return gulp.src('assets/scss/style.scss')
		.pipe(sass())
		.pipe(cleanCSS({compatibility: 'ie8'}))
		.pipe(rename({ extname: '.min.css' }))
		.pipe(gulp.dest('./static/css/'));
});

gulp.task('minify-js', function() {
	return gulp.src('./assets/js/script.js')
		.pipe(uglify())
		.pipe(rename({ extname: '.min.js' }))
		.pipe(gulp.dest('./static/js/'));
});

gulp.task('runserver', function() {
	gulp.watch('assets/scss/style.scss', ['build-css']);
	gulp.watch('assets/js/script.js', ['minify-js']);

	var runserver = spawn();
});
