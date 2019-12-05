#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

uniform float xmin;
uniform float xmax;
uniform float ymin;
uniform float ymax;
uniform float k;

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}


void main(void){
	float grx = gl_FragCoord.x / 800.0;
	float gry = gl_FragColor.y / 800.0;
	float x = (grx)*(xmax-xmin)+xmin;
	float y = (gry)*(ymax-ymin)+ymin;
	float dy = y + x;
	float angle = -atan(dy);
	float hue = (angle+1.570796)/(3.1415962);
	vec3 hsb = vec3(hue, 1.0, 1.0);
	vec3 rgb = hsv2rgb(hsb);
  gl_FragColor = vec4(vec3(rgb), 1.0);
}
