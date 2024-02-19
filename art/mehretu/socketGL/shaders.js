var vertexShaderSource = `attribute vec2 a_position;
uniform vec2 u_resolution;
uniform vec2 u_scale;
void main() {
    //scale
    vec2 scaledPosition = a_position * u_scale;
    
    // convert the position from pixels to 0.0 to 1.0
    vec2 zeroToOne = a_position / u_resolution;

    // convert from 0->1 to 0->2
    vec2 zeroToTwo = zeroToOne * 2.0;

    // convert from 0->2 to -1->+1 (clip space)
    vec2 clipSpace = zeroToTwo - 1.0;

    gl_Position = vec4(clipSpace * vec2(1, -1), 0, 1);
}`
var fragmentShaderSource = `// fragment shaders don't have a default precision so we need
// to pick one. mediump is a good default
precision mediump float;
uniform vec4 u_color;

void main() {
    // gl_FragColor is a special variable a fragment shader
    // is responsible for setting
    gl_FragColor = u_color;
}`;