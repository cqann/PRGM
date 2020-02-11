#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_TEXTURE_SHADER

varying vec4 vertTexCoord;
uniform float xmin;
uniform float xmax;
uniform float ymin;
uniform float ymax;

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

void main(void){
	vec2 pos = gl_FragCoord.xy / resolution.xy;
	float grX = (pos.x)*(xmax-xmin)+xmin;
	float grY = (pos.y)*(ymax-ymin)+ymin;
	vec2 gr = vec2(grX,grY);
	float dy = cos(k*sin(gr.y-gr.x))-sin(k*cos(gr.x+gr.y));
	float angle = -atan(dy);
	float hue = (angle+1.570796)/(3.1415962);
	vec3 hsb = vec3(hue, 1.0, 1.0);
	vec3 rgb = hsv2rgb(hsb);
  gl_FragColor = vec4(vec3(rgb), 1.0);
}
