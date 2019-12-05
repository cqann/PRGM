#ifdef GL_ES
precision mediump float;
precision mediump int;
#endif

#define PROCESSING_COLOR_SHADER
#define PI 3.14159265359
#define E  2.71828182845


uniform float min;
uniform float max;
uniform float k;
uniform float resx;
uniform float resy;

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec2 sinz(vec2 c)
{
    float a = pow(E, c.y);
    float b = pow(E,-c.y);
    return vec2(sin(c.x)*(a + b)*0.5, cos(c.x)*(a - b)*0.5);
}

vec2 cosz(vec2 c)
{
    float a = pow(E, c.y);
    float b = pow(E,-c.y);
    return vec2(cos(c.x)*(a + b)*0.5, -sin(c.x)*(a - b)*0.5);
}

vec2 tanz(vec2 c)
{
    float a = pow(E, c.y);
    float b = pow(E,-c.y);
    float cosx = cos(c.x);
    float sinhy = (a - b)*0.5;
    return vec2(sin(c.x)*cosx, sinhy*(a + b)*0.5)/(cosx*cosx + sinhy*sinhy);
}

vec2 logz(vec2 c)
{
    return vec2(log(sqrt(dot(c, c))), atan(c.y, c.x));
}

vec2 sqrtz(vec2 c)
{
    float n = c.x + sqrt(dot(c, c));
    return vec2(n, c.y)/sqrt(2.0*n);
}

vec2 exp2z(vec2 c)
{
	return vec2(c.x*c.x - c.y*c.y, 2.*c.x*c.y);
}

vec2 epowz(vec2 c)
{
	return vec2(cos(c.y), sin(c.y))*pow(E, c.x);
}

vec2 mulz(vec2 c1, vec2 c2)
{
    return c1*mat2(c2.x, -c2.y, c2.y, c2.x);
}

vec2 divz(vec2 n, vec2 d)
{
    return n*mat2(d.x, d.y, -d.y, d.x)/dot(d, d);
}

vec2 invz(vec2 c)
{
	return vec2(c.x, -c.y)/dot(c, c);
}


void main(void){
  vec2 res = vec2(resx,resy);
	vec2 pos = gl_FragCoord.xy/res;


  //float a = pos.x*(max-min)+min;
  //float b = pos.y*(max-min)+min;
  vec2 z = vec2(pos.x*(max-min)+min,pos.y*(max-min)+min);

  //float opa = a;
  //float opb = b;
  vec2 fz = mulz( vec2(z.x*cos(k),z.y-3*cos(k)),vec2(z.y,sin(k)) );
  float absz = length(z);


  float hue = atan(fz.y,fz.x)/(2.0*3.1415962);
  float val = 1 - pow(0.1,absz);

  vec3 hsv = vec3(hue,1.0,val);
  vec3 rgb = hsv2rgb(hsv);

  gl_FragColor = vec4(rgb, 1.0);
}



/*
mulz(mulz(z,mulz(z,z)),divz(z,cosz(z+cos(k))))
mulz(mulz(tanz(z),sinz(z)),cosz(z))-cos(k)
divz(z,vec2(5*cos(k),-z.x))
vec2(-z.y*z.x,sin(k)*cos(k-z.y))

*/
