<script lang="ts">
	import { cn } from '$utils';
	import {
		Accordion,
		type AccordionContentProps,
		type WithoutChild,
	} from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		children,
		...props
	}: WithoutChild<AccordionContentProps> = $props();
</script>

<Accordion.Content
	bind:ref
	class={cn(
		'data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down overflow-hidden text-sm',
		className,
	)}
	{...props}
>
	<div class="pb-4 pt-0">
		{@render children?.()}
	</div>
</Accordion.Content>
