'use strict';

var gulp = require('gulp');
var rename = require('gulp-rename');
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');
var os = require('os');
var spawn = require('child_process').spawn;

gulp.task('build-css', function() {
	return gulp.src('static/scss/style.scss')
		.pipe(sass())
		.pipe(cleanCSS({compatibility: 'ie8'}))
		.pipe(rename({ extname: '.min.css' }))
		.pipe(gulp.dest('static/css/'));
});

gulp.task('build-js', function() {
	return gulp.src('static/js/script.js')
		.pipe(uglify())
		.pipe(rename({ extname: '.min.js' }))
		.pipe(gulp.dest('static/js/'));
});

gulp.task('runserver', ['build-css', 'build-js'], function() {
	gulp.watch('static/scss/style.scss', ['build-css']);
	gulp.watch('static/js/script.js', ['build-js']);

	// Compatibility across all platforms
	const pythonPath = (os.platform() === 'win32' ? '/scripts/' : '/bin/') + 'python';

	var runserver = spawn(
		process.env['VIRTUAL_ENV'] + pythonPath, ['manage.py', 'runserver'], { stdio: 'inherit' }
	);

	runserver.on('close', function(code) {
		if(code !== 0) {
			console.error('Django runserver exited with error code: ' + code);
		} else {
			console.log('Django runserver exited normally.');
		}
	});
});
