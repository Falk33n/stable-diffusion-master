import { untrack } from 'svelte';

const MOBILE_BREAKPOINT = 768;

export class IsMobile {
	#current = $state<boolean>(false);

	constructor() {
		$effect(() => {
			return untrack(() => {
				const mediaQuery = matchMedia(
					`(max-width: ${MOBILE_BREAKPOINT - 1}px)`,
				);

				const onChange = () => {
					this.#current = innerWidth < MOBILE_BREAKPOINT;
				};
				onChange();

				mediaQuery.addEventListener('change', onChange);
				return () => {
					mediaQuery.removeEventListener('change', onChange);
				};
			});
		});
	}

	get current() {
		return this.#current;
	}
}
