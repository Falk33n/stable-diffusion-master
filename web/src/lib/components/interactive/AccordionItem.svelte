<script lang="ts">
	import { cn } from '$utils';
	import { Accordion, type AccordionItemProps } from 'bits-ui';

	let {
		ref = $bindable(null),
		class: className,
		...props
	}: AccordionItemProps = $props();
</script>

<Accordion.Item
	bind:ref
	class={cn('border-b', className)}
	{...props}
/>
