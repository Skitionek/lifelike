// Module augmentation to restore d3 v5 APIs (d3.event and d3.mouse) that were
// removed in d3 v6+. The graph viewer code was written against the d3 v5 API.
import 'd3';

declare module 'd3' {
  // d3.event was removed in d3 v6; it held the current DOM event during a d3 callback
  const event: any;

  // d3.mouse was removed in d3 v6; replaced by d3.pointer(event, container)
  function mouse(container: Element | SVGElement): [number, number];
}
