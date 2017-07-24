'use strict';

var gulp = require('gulp');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');
var spawn = require('child_process').spawn;

gulp.task('build-css', function() {
	return gulp.src('assets/scss/style.scss')
		.pipe(sass())
		.pipe(cleanCSS({compatibility: 'ie8'}))
		.pipe(rename({ extname: '.min.css' }))
		.pipe(gulp.dest('./static/css/'));
});

gulp.task('build-js', function() {
	return gulp.src('./assets/js/script.js')
		.pipe(uglify())
		.pipe(rename({ extname: '.min.js' }))
		.pipe(gulp.dest('./static/js/'));
});

gulp.task('runserver', function() {
	gulp.watch('assets/scss/style.scss', ['build-css']);
	gulp.watch('assets/js/script.js', ['build-js']);

	var runserver = spawn(
		process.env['VIRTUAL_ENV'] + '/bin/python',
		['manage.py', 'runserver', '--settings=project_name.settings.development'],
		{ stdio: 'inherit' }
	);

	runserver.on('close', function(code) {
		if(code !== 0) {
			console.error('Django runserver exited with error code: ' + code);
		} else {
			console.log('Django runserver exited normally.');
		}
	});
});
