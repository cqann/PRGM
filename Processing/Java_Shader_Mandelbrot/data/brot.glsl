#ifdef GL_ES
precision mediump int;
#endif

#define PROCESSING_COLOR_SHADER

uniform float xmin;
uniform float xmax;
uniform float ymin;
uniform float ymax;
uniform float limit;


vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}


void main(void){
   vec2 uv = vec2(gl_FragCoord.x/800.0,gl_FragCoord.y/800.0);

   float zre = 0.0;
   float zim = 0.0;
   float cre = (uv.x * (xmax-xmin))+xmin;
   float cim = (uv.y * (ymax-ymin))+ymin;
   float count = 0.0;


   for(float i = 0.0;i<limit;i++){
       float zsqre = zre*zre - zim*zim;
       float zsqim = 2.0*zre*zim;
       zre = zsqre + cre;
       zim = zsqim + cim;
       count = count + 1.0;
       if(zre*zre + zim*zim > 4.0){
         break;
       }
   }

   vec3 hsbcol = vec3(count*0.01,1.0,1.0);

   vec3 col = hsv2rgb(hsbcol);

   if(count + 0.1 > limit){
      col = vec3(0.0,0.0,0.0);
   }

   // Output to screen
   gl_FragColor = vec4(col,1.0);
}
